from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username='tester',
            email='tester@example.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'tester')
        self.assertEqual(user.email, 'tester@example.com')
        self.assertEqual(user.password, 'testpass123')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superdave',
            email='superdave@example.com',
            password='testpass123',
        )
        self.assertEqual(admin_user.username, 'superdave')
        self.assertEqual(admin_user.email, 'superdave@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
