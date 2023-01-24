from django.contrib.auth.models import User
from .models import Comment
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class CommentListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_comment(self):
        adam = User.objects.get(username='adam')
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_comment(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        response = self.client.post(
            '/comments/',
            {'post': 1,
             'content': 'a comment'
             })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_comment(self):
        response = self.client.post(
            '/comments/',
            {'content': 'a comment'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ConnetViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        paul = User.objects.create_user(username='paul', password='pass')
        Post.objects.create(
            owner=adam, title='adams title', content='adams content'
        )
        Post.objects.create(
            owner=adam, title='pauls title', content='pauls content'
        )
        Comment.objects.create(
            post_id=1,
            owner=adam, content='adam comment'
        )
        Comment.objects.create(
            post_id=2,
            owner=paul, content='paul comment'
        )

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'adam comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/comments/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_comment(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/comments/1/',
            {'content':
             'a new comment'
             })
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'a new comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_comment(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/comments/2/',
            {'content':
             'add a new comment'
             })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
