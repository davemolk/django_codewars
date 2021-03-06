from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class CustomUserTests(TestCase):

    def test_create_user(self):
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

class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, "Should not be on page")
    
    def test_signup_form(self):
        new_user = User.objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                        [0].email, self.email)

