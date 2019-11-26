from django.test import TestCase
from django.contrib.auth import get_user_model
from model_mommy import mommy
from ...models import Form
from ...viewsets import FormViewset

User = get_user_model()


class FormViewsetTest(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username="test")
        self.form = mommy.make(Form, creator=self.user)

    def test_form_ownership(self):
        user_two = mommy.make(User, username="test2")
        self.assertTrue(self.user, self.form.creator)
        self.assertNotEqual(user_two, self.form.creator)

    def test_form_creation(self):
        forms_len = Form.objects.count()
        self.assertEqual(forms_len, 1)
