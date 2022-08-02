# {{ cookiecutter.app_name }}

TODO: description

## Generating a new project

### Render project

To render a new project using this cookiecutter template, run the following:

```sh
cookiecutter gh:parrot-com/cookiecutter-python
```

### Manual steps

You need to manually perform the following steps:

1. create a GitHub repository
    * add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to the "Settings -> Secrets -> Actions"
1. create a Sentry project
    * TODO: set env variables
1. create ECR repository
1. TODO: add k8s manifests

## TODO

* different .env files
* docker-compose.yaml
* run app without pip install /app (https://github.com/parrot-com/sample/pull/1#discussion_r881742478)
* use GHA cache (https://github.com/parrot-com/sample/pull/1#discussion_r871690106)
* run linters using pre-commit (https://github.com/parrot-com/sample/pull/1#discussion_r871692033)
* install poetry the right way (https://github.com/parrot-com/sample/pull/1#discussion_r871697099)
* add multistage builds (https://github.com/parrot-com/sample/pull/1#discussion_r869128031)
* use venv (https://github.com/parrot-com/sample/pull/1#discussion_r869128224)
* better loggers by default (https://github.com/parrot-com/sample/pull/1#discussion_r877155269)
* switch to alpine (https://github.com/parrot-com/sample/pull/1#discussion_r877163909)
* notes on how to run tests, black, isort, flake8
* try https://pypi.org/project/Flake8-pyproject/ instead of this
