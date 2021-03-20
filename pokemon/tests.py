from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Pokemon

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Pokemon.objects.create(
            trainer = testuser1,
            name = 'Green Eggs and Ham',
            description = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_post.save()

    def test_pokemon_content(self):
        post = Pokemon.objects.get(id=1)
        actual_trainer = str(post.trainer)
        actual_name = str(post.name)
        actual_description = str(post.description)
        self.assertEqual(actual_trainer, 'testuser1')
        self.assertEqual(actual_name, 'Green Eggs and Ham')
        self.assertEqual(actual_description, 'I do not like green eggs and ham, Sam I  am.')