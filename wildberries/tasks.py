import requests
from celery import shared_task
from rest_framework import status

from config.logger import logger


@shared_task
def parse_wb_product_by_article(article):
    try:
        url = f"https://card.wb.ru/cards/v2/detail?appType=1&curr=byn&dest=-1257786&spp=30&ab_testing=false&nm={article}"
        response = requests.get(url=url)

        if not response.json()["data"]["products"]:
            logger.error(f"Product with article {article} does not exist")
            return {
                "error": f"Product with article {article} does not exist",
                "status": status.HTTP_404_NOT_FOUND,
            }

        data = response.json()["data"]["products"][0]

        product = {
            "article": article,
            "name": data["name"].strip(),
            "brand": data["brand"].strip(),
            "supplier": data["supplier"].strip(),
            "basic_price": (
                float(data["sizes"][0]["price"]["basic"]) / 100 if "price" in data["sizes"][0] else None
            ),
            "sale_price": (
                float(data["sizes"][0]["price"]["product"]) / 100 if "price" in data["sizes"][0] else None
            ),
            "total_quantity": int(data["totalQuantity"]),
            "review_rating": float(data["reviewRating"]) if "reviewRating" in data else None,
        }

        return {"product": product}

    except Exception as e:
        logger.error(f"Failed to fetch data from the site: {str(e)}")
        return {"error": "Failed to fetch data from the site", "status": status.HTTP_400_BAD_REQUEST}
