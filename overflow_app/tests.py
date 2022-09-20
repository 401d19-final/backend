from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Question,Comment

class QuestionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass