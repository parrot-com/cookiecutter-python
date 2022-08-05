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
1. create a Sentry project
    * TODO: set env variables
1. create ECR repository
1. TODO: add k8s manifests

## TODO

* different .env files
* docker-compose.yaml
* use GHA cache (https://github.com/parrot-com/sample/pull/1#discussion_r871690106)
* run linters using pre-commit (https://github.com/parrot-com/sample/pull/1#discussion_r871692033)
* better loggers by default (https://github.com/parrot-com/sample/pull/1#discussion_r877155269)
* notes on how to run tests, black, isort, flake8
