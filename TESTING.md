# Testing For API foodSNAP

back to the [README.md](README.md)

## Contents
-   [Automated Unit Testing](#unit-testing)
    -   [foodSNAP List View](#foodsnap-list-view)
    -   [foodSNAP Detail View](#foodsnap-detail-view)
    -   [Recipe View](#recipe-view)
    -   [Comments View](#comments-view)
-  [Validator Testing](#validator-testing)
-   [Manual Testing](#manual-testing)
    -   [URL Path tests](#url-path-tests)
    -   [Search and Filter testing](#search-and-filter-testing)
    -   [CRUD Testing](#crud-testing)

## Automated Unit Testing
- I have used API Testcase to test the views using a red, green refactor method.
<br />

### Posts List View
- Created 3 tests to make sure users can retrieve all foodSNAPS a logged in user can update their
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

- results all passed

![Results for foodSNAP list view](/documentation/screenshots/foodsnap-tests.webp)


### foodSNAP Detail View
- Created 4 tests to check that a valid id will retrieve an foodSNAP, an invalid id will not retrieve an
foodSNAP, check wether a user can update their own foodSNAP, and a foodSNAP cannot be updated by someone
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

### Profile View
- Created 4 tests to check that a valid id will retrieve a profile an invalid id will not retrieve a
profile and check wether a user can update their own profile.

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
```

- All tests passed

![Testing prfofile view](/documentation/screenshots/profile-test.webp)

### Recipe View
- Tests to check that a valid id will retrieve a recipe, an invalid id will not retrieve a
recipe, check wether a user can update their own recipe, and a recipe cannot be updated by someone
who doesn't own it.

![Testing recipe detail view](/documents/readme_images/test-recipe-detail.webp)


- All tests passed

![results for recipe detail view](/documents/readme_images/results-recipe-detail.webp)

### Comments View
- Tests to check that a valid id will retrieve a comment, an invalid id will not retrieve a
comment check wether a user can update their own comment, and a comment cannot be updated by someone
who doesn't own it.

![Tests for comment detail view](/documents/readme_images/test-comment-detail.webp)

- All tests passed

![Results for comment detail view tests](/documents/readme_images/results-comment-detail.webp)

## Validator Testing
- Files from the project were run through the online pep8 validator, as each one was checked I marked it
off on a table, There were 3 errors, one was found from the validator, which was no new line at the end of the file, the other two was line too long which was corrected before running through the validator.

![Validator table for checking](./assets/documents/p5-pep8-testing-table.png)

![Error found in pep8 validator](./assets/documents/error-pep8-url.png)

## Manual Testing
- Manual Tests were carried out for the URL routes, search and filter functionality, and CRUD functionality.

### URL route tests

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

back to the [README.md](README.md)