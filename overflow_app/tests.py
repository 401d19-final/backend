from django.test import TestCase
from .models import Question, Comment
from django.contrib.auth import get_user_model


# Create your tests here.
class QuestionCommentTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass1")
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(username="testuser2", password="pass2")
        testuser2.save()

        test_question = Question.objects.create(username=testuser1, title="This is a test question title?", content="This is an answer or comment for the test question")
        test_question.save()
        test_comment = Comment.objects.create(question=test_question, username=testuser2,  content="This is an answer or comment")
        test_comment.save()

    def test_questions_model(self):
        question_1 = Question.objects.get(id=1)
        actual_username = str(question_1.username)
        actual_title = str(question_1.title)
        actual_content = str(question_1.content)
        self.assertEqual(actual_username, "testuser1")
        self.assertEqual(actual_title, "This is a test question title?")
        self.assertEqual(actual_content, "This is an answer or comment for the test question")

    def test_comments_model(self):
        comment_1 = Comment.objects.get(id=1)
        actual_username = str(comment_1.username)
        actual_content = str(comment_1.content)
        self.assertEqual(actual_username, "testuser2")
        self.assertEqual(actual_content, "This is an answer or comment")