from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from config.logger import logger
from wildberries.models import Product
from wildberries.serializers import ArticleSerializer, ProductSerializer
from wildberries.tasks import parse_wb_product_by_article


class ProductViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.validated_data.get("article")

        if Product.objects.filter(article=article).exists():
            return Response(
                data={"message": f"Product with article {article} already exists in the database"},
                status=status.HTTP_302_FOUND,
            )

        task = parse_wb_product_by_article.delay(article)

        try:
            result = task.get()

            if "error" in result:
                return Response(data={"error": result["error"]}, status=result["status"])

            new_product = ProductSerializer(result.get("product")).data

            Product.objects.create(**new_product)

            return Response(
                data={"message": f"Product with article {article} successfully saved in the database"},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            logger.error(f"Failed to fetch data from the site and create the product: {str(e)}")
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            product_list = ProductSerializer(self.get_queryset(), many=True)

            if not product_list:
                logger.error("No products in the database found")
                return Response(
                    data={"message": "No products in the database found"}, status=status.HTTP_404_NOT_FOUND
                )

            return Response(product_list.data)

        except Exception as e:
            logger.error(f"Failed to get product list from the database: {str(e)}")
            return Response(
                data={"error": "Failed to get product list from the database"},
                status=status.HTTP_400_BAD_REQUEST,
            )
