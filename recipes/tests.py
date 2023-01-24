from django.contrib.auth.models import User
from .models import Recipe
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class RecipeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_recipe(self):
        adam = User.objects.get(username='adam')
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_recipe(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        response = self.client.post(
            '/recipes/',
            {'post': 1,
             'ingredients': 'ingredients',
             'method': 'method'
             })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_recipe(self):
        response = self.client.post(
            '/recipes/',
            {'ingredients': 'ingredients',
             'method': 'method'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecipeViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        paul = User.objects.create_user(username='paul', password='pass')
        Post.objects.create(
            owner=adam, title='a title', content='adams content'
        )
        Post.objects.create(
            owner=adam, title='pauls title', content='pauls content'
        )
        Recipe.objects.create(
            post_id=1,
            owner=adam, ingredients='ingredients', method='method'
        )
        Recipe.objects.create(
            post_id=2,
            owner=paul, ingredients='ingredients', method='method'
        )

    def test_can_retrieve_recipe_using_valid_id(self):
        response = self.client.get('/recipes/1/')
        self.assertEqual(response.data['ingredients'], 'ingredients')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_recipe_using_invalid_id(self):
        response = self.client.get('/recipes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_recipe(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/recipes/1/',
            {'ingredients':
             'a new title',
             'method': 'method'
             })
        recipe = Recipe.objects.filter(pk=1).first()
        self.assertEqual(recipe.ingredients, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_recipe(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/recipes/2/',
            {'ingredients':
             'a new title',
             'method': 'method'
             })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
