from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView, ProfilePageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('pages:home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Home')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Throw error')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__,
        )

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('pages:about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Throw error')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__,
        )

class ProfilePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('pages:profile')
        self.response = self.client.get(url)

    def test_profilepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_profilepage_template(self):
        self.assertTemplateUsed(self.response, 'profile.html')

    def test_profilepage_contains_correct_html(self):
        self.assertContains(self.response, 'Profile')

    def test_profilepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Throw error')

    def test_profilepage_url_resolves_profilepageview(self):
        view = resolve('/profile/')
        self.assertEqual(
            view.func.__name__,
            ProfilePageView.as_view().__name__,
        )