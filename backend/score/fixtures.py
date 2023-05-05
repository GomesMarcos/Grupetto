import os

import django
from model_bakery import baker
from pytest import fixture

# Setting up DJANGO_SETTINGS_MODULE for pytest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")
django.setup()
if True:
    from rest_framework.test import APIRequestFactory


@fixture
def factory():
    return APIRequestFactory()


@fixture
def mock_player():
    return baker.make("score.Player")


@fixture
def mock_score(mock_player):
    return baker.make("score.Score", player=mock_player)
