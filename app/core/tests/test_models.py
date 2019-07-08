from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Creando test de usuario con email"""
        email = "cesardjango@test.com"
        password = "TestPass1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalizaed(self):
        """ Normaliza email"""
        email = "cesardjango@TEST.com"
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Email Invalido"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """Test para crear nuevo superusuario"""
        user = get_user_model().objects.create_superuser(
            'cesardjango@test.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
