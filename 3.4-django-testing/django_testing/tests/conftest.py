import os

import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student
from students.models import Course

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_testing.settings'

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

