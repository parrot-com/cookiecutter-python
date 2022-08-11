# {{ cookiecutter.app_name }}

{{ cookiecutter.description }}

## Local development

How to run tests:

```sh
docker compose exec -e APP_ENV=test {{ cookiecutter.app_nae }} pytest
```

How to run black:

```sh
docker compose exec remote_ml black /app
```

How to run isort:

```sh
docker compose exec remote_ml isort /app
```

How to run flake8:

```sh
docker compose exec remote_ml flake8
```
