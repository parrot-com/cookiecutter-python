# {{ cookiecutter.app_name }}

{{ cookiecutter.description }}

## Local development

How to run tests:

```sh
docker compose exec -e APP_ENV=test {{ cookiecutter.app_name }} pytest
```

How to run black:

```sh
docker compose exec {{ cookiecutter.app_name }} black /app
```

How to run isort:

```sh
docker compose exec {{ cookiecutter.app_name }} isort /app
```

How to run flake8:

```sh
docker compose exec {{ cookiecutter.app_name }} flake8
```

How to run mypy:

```sh
docker compose exec {{ cookiecutter.app_name }} mypy /app
```
