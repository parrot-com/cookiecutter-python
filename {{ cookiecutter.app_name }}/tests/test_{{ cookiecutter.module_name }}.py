import pytest

from {{ cookiecutter.module_name }}.config import settings


# example: this is how you would override settings when running tests
@pytest.mark.override_settings.with_args(app_env="production")
def test_it_overrides_env():
    assert settings.app_env == "production"
