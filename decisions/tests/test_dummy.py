import pytest
from django.apps import apps


@pytest.mark.django_db
def test_apps_exist():
    assert list(apps.get_models())
