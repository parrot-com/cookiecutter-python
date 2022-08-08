import pytest

from {{ cookiecutter.app_name }}.config import settings


@pytest.fixture(autouse=True)
def override_settings(request):
    # get overrides from the pytest marker
    mark = request.node.get_closest_marker("override_settings")
    overrides = mark.kwargs if mark else {}

    # capture original settings' values
    original = {override: getattr(settings, override) for override in overrides}

    # override settings
    for key, value in overrides.items():
        setattr(settings, key, value)

    # run test
    yield

    # restore original settings
    for override in overrides.keys():
        setattr(settings, override, original[override])
