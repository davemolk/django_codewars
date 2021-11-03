from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Exercise


User = get_user_model()


class ExerciseTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123',
        )
        self.kata = Exercise.objects.create(
            owner=self.user,
            name='my kata',
            cw_id='123qweR',
            languages='python',
            description='a hard kata',
            tags='tdd',
            rank='1 kyu',
            url='www.google.com',
            notes='i aced this',
        )
    
    def test_kata_listing(self):
        self.assertEqual(f'{self.kata.owner.username}', 'testuser')
        self.assertEqual(f'{self.kata.name}', 'my kata')
        self.assertEqual(f'{self.kata.cw_id}', '123qweR')
        self.assertEqual(f'{self.kata.languages}', 'python')
        self.assertEqual(f'{self.kata.description}', 'a hard kata')
        self.assertEqual(f'{self.kata.tags}', 'tdd')
        self.assertEqual(f'{self.kata.rank}', '1 kyu')
        self.assertEqual(f'{self.kata.url}', 'www.google.com')
        self.assertEqual(f'{self.kata.notes}', 'i aced this')
