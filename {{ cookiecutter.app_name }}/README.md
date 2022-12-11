# {{ cookiecutter.app_name }}

{{ cookiecutter.description }}

## Installation

Follow these steps:

1. Make a copy of the environment file & fill in the variables.
   ```sh
   cp .env.example .env
   ```
2. Start the service
   ```
   docker compose up
   ```

And that's it.

## Local development

How to add a new package:

```sh
docker compose exec {{ cookiecutter.app_name }} poetry add package_name
```

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
