from django.test import TestCase
from django.contrib.auth import get_user_model
from model_mommy import mommy
from ...models import Question, Form
from ...viewsets import QuestionViewSet

User = get_user_model()


class QuestionViewsetTest(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username="test")
        self.form = mommy.make(Form, creator=self.user)
        self.question = mommy.make(Question, form=self.form)

    def test_form_creation(self):
        question_len = Question.objects.count()
        self.assertEqual(question_len, 1)

    def test_form_relation(self):
        form2 = mommy.make(Form, creator=self.user)
        self.assertEqual(self.form, self.question.form)
        self.assertNotEqual(form2, self.question.form)
