# cookiecutter-python

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
    * trigger error on staging and production and then create [alert rules](https://docs.sentry.io/product/integrations/notification-incidents/slack/) to our monitoring channels on Slack
1. create ECR repository
1. TODO: add k8s manifests
    * set Helm chart env variables (you will probably want to set `APP_ENV` or similar variable when the project is used in multiple environments)

## TODO

* [ ] different .env files
* [ ] docker-compose.yaml
* [ ] run linters using pre-commit
