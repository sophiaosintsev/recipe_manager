from django.test import TestCase
from django import forms
from django.contrib.auth.models import User

from .forms import UserForm


class TestUserForm(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'sophia',
            'last_name': 'osintsev',
            'username': 'sophiaosintsev',
            'email': 'sofica05@gmail.com',
            'password1': 'admin123',
            'password2': 'admin123',
        }

    def test_password_if_short(self):

        form = forms.UserForm(self.data)
        self.assertTrue(form.is_valid())

        data = self.data
        data['password1'] = 'admin'
        data['password2'] = 'admin'
        form = forms.UserForm(data)
        self.assertFalse(form.is_valid())

        self.assertEqual(
            form.errors,
            {'password1': ['Must be more than 7 characters long!']}
        )

    def test_user_on_save(self):
        self.assertEqual(User.objects.count(), 0)

        form = forms.UserForm(self.data)
        form.save()

        self.assertEqual(User.objects.count(), 1)


class TestPasswordIfMatching(TestCase):

    def test_has_capital(self):
        result = forms.has_capital('a')
        self.assertFalse(result)

        result = forms.has_capital('A')
        self.assertTrue(result)

        result = forms.has_capital('@')
        self.assertFalse(result)

        result = forms.has_capital(' ')
        self.assertFalse(result)
