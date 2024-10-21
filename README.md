# Stuttgart Center Task

## Quickstart

1. To set up the project please create new directory **StuttgartCenterTask** on your computer and clone the git repository using the command:

```console
$ git clone https://github.com/igorkartel/StuttgartCenterTask.git .
```

2. Then open the project in your IDE (PyCharm or VSCode). A virtual environment for this project must be built with **poetry**.
Find the file **pyproject.toml** with all dependencies and change the python version you are using in this line:
**python = "^3.11"** (you can choose "3.10", "3.11" or "3.12" only; I used "3.12", so it is configured as default).

3. Create in the project root your **.env** file. You can see the parameters to define in the file **env_config.py**.

4. Create poetry virtual environment and install the dependencies.

5. Then run in your IDE console the following command to initialize a container with all the services:

```console
$ docker compose up -d --build
```

6. Now the project is ready for use.
You can see generated docs by following links: http://localhost:8002/docs
