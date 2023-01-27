<h1 id="top">Testing For API foodSNAP</h1>

back to the [README.md](README.md)

## Contents
-   [Automated Unit Testing](#unit-testing)
    -   [foodSNAP View](#foodsnap-view)
    -   [Profile View](#profile-view)
    -   [Recipe View](#recipe-view)
    -   [Comments View](#comments-view)
-  [Manual Testing](#manual-testing)
    -   [API Endpoint Tests](#api-endpoint-tests)
    -   [Search and Filter testing](#search-and-filter-testing)
    -   [CRUD Testing](#crud-testing)
-  [Validator Testing](#pycodestyle-validator-testing)
-  [Bugs](#bugs)
    -   [Fixed](#fixed)
    -   [Unfixed](#unfixed)

## Automated Unit Testing

- API Testcase was utilised to test the views and the coverage report was 86% before tests where created.

![Original coverage report](/documentation/screenshots/original-coverage.webp)

<br />

- 26 new tests where created and tests were run, the coverage report is now 95%, this could of course be improved to 100% and would be something to consider in the future.

![Final coverage report](/documentation/screenshots/final-coverage.webp)

<br />

### foodSNAP View
- Created 3 tests to make sure users can retrieve all foodSNAPS, a logged in user can update their
foodSNAPS and a logged out user cannot create a foodSNAP.

```
class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_posts(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

- Created 4 tests to check that a valid id will retrieve an foodSNAP, an invalid id will not retrieve an
foodSNAP, check if a user can update their own foodSNAP, and a foodSNAP cannot be updated by someone
who doesn't own it.

```
class PostDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Post.objects.create(
            owner=adam, title='a title', content='adams content'
        )
        Post.objects.create(
            owner=brian, title='another title', content='brians content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

- All tests passed

![Results for foodSNAP detail view](/documentation/screenshots/foodsnap-tests.webp)

<a href="#top">Back to the top.</a>

### Profile View
- Created 5 tests to check that a valid id will retrieve a profile, an invalid id will not retrieve a
profile, check if a user can update their own profile and a profile cannot be updated by someone
who doesn't own it.

```
class ProfileListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_profile(self):
        adam = User.objects.get(username='adam')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        paul = User.objects.create_user(username='paul', password='pass')

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.data['owner'], 'adam')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_profile(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/profiles/1/', {'name': 'paul'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'paul')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_profile(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/profiles/2/',
            {'owner': 'paul'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

- All tests passed

![Testing prfofile view](/documentation/screenshots/profile-tests.webp)

<a href="#top">Back to the top.</a>

### Recipe View

- Created 3 tests to make sure users can retrieve all recipes, a logged in user can update their
recipe and a logged out user cannot create a recipe.

```
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
```

- Created 4 tests to check that a valid id will retrieve a recipe, an invalid id will not retrieve a
recipe, check if a user can update their own recipe, and a recipe cannot be updated by someone
who doesn't own it.

```
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

```

- All tests passed

![results for recipe detail view](/documentation/screenshots/recipes-tests.webp)

<a href="#top">Back to the top.</a>

### Comments View

- Created 3 tests to make sure users can retrieve all comments, a logged in user can update their
comment and a logged out user cannot create a comment.

```
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
```


- Created 4 tests to check that a valid id will retrieve a comment, an invalid id will not retrieve a
comment, check if a user can update their own comment, and a comment cannot be updated by someone
who doesn't own it.

```
class CommentViewTests(APITestCase):
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
```

- All tests passed

![Results for comment detail view tests](/documentation/screenshots/comments-tests.webp)

<a href="#top">Back to the top.</a>


## Manual Testing
- Manual Tests were carried out for the API Endpoints, search and filter functionality, and CRUD functionality.

### API Endpoint Tests

|   URL Route   | Deployed Check |
|:-------------:|:--------------:|
|    /posts/    |      Works     |
|   /posts/4/   |      Works     |
|   /profiles/  |      Works     |
|  /profiles/5/ |      Works     |
|   /comments/  |      Works     |
|  /comments/3/ |      Works     |
|   /recipes/   |      Works     |
|  /recipes/4/  |      Works     |
|    /likes/    |      Works     |
|   /likes/3/   |      Works     |
|  /followers/  |      Works     |
| /followers/2/ |      Works     |
|       /       |      Works     |

### Search and Filter testing

|    Item   | Search                                               | Filter Liked                                                                       | Filter Followed                                                                           | Filter Own Posts                                                                      |
|:---------:|------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| foodSNAPS | working can search by keyword in title and username  | working the liked page updates and removes foodSNAPS based on if it's liked or not | working the feed page updates and removes foodSNAPS based on if a user is followed or not | working the profile page displays all foodSNAPS created by the current logged in user |
|           |                                                      |                                                                                    |                                                                                           |                                                                                       |

<a href="#top">Back to the top.</a>

### CRUD Testing
- The table below was created to check a user could Create, Read, Edit, or Delete items.
- I used a key in the table 
    - L meaning the user was logged in and could create, and read.
    - O meaning the user was not logged in and could only read.
    - LO meaning the user was logged in, is the owner and had full CRUD functionality.

|   Item   |      Read      | Create                   | Edit                     | Delete                   |
|:--------:|:--------------:|--------------------------|--------------------------|--------------------------|
| foodSNAP | L = Y<br>O = Y | L = Y<br>O = N           | L = N<br>O = N<br>LO = Y | L = N<br>O = N<br>LO = Y |
| Like     | L = Y<br>O = Y | L = Y<br>O = N           | L = N<br>O = N<br>LO = Y | L = N<br>O = N<br>LO = Y |
| Comment  | L = Y<br>O = Y | L = Y<br>O = N           | L = N<br>O = N<br>LO = Y | L = N<br>O = N<br>LO = Y |
| Recipe   | L = Y<br>O = N | L = N<br>O = N<br>LO = Y | L = N<br>O = N<br>LO = Y | L = N<br>O = N<br>LO = Y |
| Profile  | L = Y<br>O = Y | L = Y<br>O = N<br>LO = N | L = N<br>O = N<br>LO = Y | L = N<br>O = N<br>LO = N |
| Follow   | L = Y<br>O = N | L = Y<br>O = N           | L = N<br>O = N<br>LO = Y | L = N<br>O = N<br>LO = Y |

<a href="#top">Back to the top.</a>

## pycodestyle Validator Testing
- Installed pycodestyle to validate the code and fixed any issues flagged during development all code validates without errors.

_ Settings.py has 4 errors with line to long but as these are AUTH_PASSWORD_VALIDATORS I can't shorten them so have not corrected this notification.

| App       | Models.py | Serializers.py | Urls.py | Views.py |
|-----------|-----------|----------------|---------|----------|
| Posts     |    PASS   |      PASS      |   PASS  |   PASS   |
| Profiles  |    PASS   |      PASS      |   PASS  |   PASS   |
| Recipes   |    PASS   |      PASS      |   PASS  |   PASS   |
| Likes     |    PASS   |      PASS      |   PASS  |   PASS   |
| Followers |    PASS   |      PASS      |   PASS  |   PASS   |
| Comments  |    PASS   |      PASS      |   PASS  |   PASS   |

## Bugs

<a href="#top">Back to the top.</a>

### Fixed
BUG: Cors Header error when signing in access not allowed
<br />
<a href="https://github.com/artcuddy/project5-foodsnap-backend/issues/8">Github Issue #8</a>

This was resolved by adding the following to the settings.py

```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(
        r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE
    ).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]

CORS_ALLOW_CREDENTIALS = True
```

BUG: Uploaded images are to big when uploaded from a mobile
<br />
<a href="https://github.com/artcuddy/project5-foodsnap-backend/issues/9">Github Issue #9</a>

Sorted this by installing https://pypi.org/project/django-resized/ and adding the below to the app settings

```
DJANGORESIZED_DEFAULT_SIZE = [622, 622]
DJANGORESIZED_DEFAULT_QUALITY = 90
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True
```
Then on the Post model changed the image field to the below
```
image = ResizedImageField(
size=[622, 622],
upload_to='images/',
default='../default-placeholder_m2h1kl',
blank=True
)
```
All images are now resized to 622px wide or high on upload

BUG: There is a bug in dj-rest-auth that doesn't allow users to log out
<br />
<a href="https://github.com/artcuddy/project5-foodsnap-backend/issues/14">Github Issue #14</a>

Solution was provide by Code Institute Moments tutorial and in the CI Slack channel

1. In foodsnap_api views.py import JWT_AUTH from settings.py
```
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
```
2. Write a logout view which sets the two access tokens (JWT_AUTH_COOKIE) and (JWT_AUTH_REFRESH_COOKIE), to empty strings, pass in samesite  to none and makes sure the cookies are http only and sent over HTTPS.
```
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
```
3. In the main **urls.py** file import the logout route
```
from .views import root_route, logout_route
```
4. Include it in the main url patterns list(must be above the default dj-rest-auth)
```
path('dj-rest-auth/logout/', logout_route),
```


### Unfixed
- None found at the time of submission


back to the [README.md](README.md)

<a href="#top">Back to the top.</a>