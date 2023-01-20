# Testing For API foodSNAP

back to the [README.md](README.md)

## Contents
1. [Unit Testing](#unit-testing)
    1. [Achievements List View](#achievements-list-view)
    2. [Achievements Detail View](#achievements-detail-view)
    3. [Memo_posts List View](#memo_posts-list-view)
    4. [Memo_posts Detail View](#memo_posts-detail-view)
    5. [Todo List View](#todo-list-view)
    6. [Todo Detail View](#todo-detail-view)
2. [Validator Testing](#validator-testing)
3. [Manual Testing](#manual-testing)
    1. [URL Path tests](#url-path-tests)
    2. [Search and Filter testing](#search-and-filter-testing)
    3. [CRUD Testing](#crud-testing)

## Unit Testing
- I have used API Testcase to test the views using a red, green refactor method.
### Achievements List View
- Tests to make sure users can retrieve all achievements, a logged in user can update their
achievements, and a logged out user cannot create an achievement.

![Testing achievements list view](./assets/documents/test-achievement-list.png)

- results all passed
![Results for achievements list view](./assets/documents/results-achievements-list.png)


### Achievements Detail View
- Tests to check that a valid id will retrieve an achievement post, an invalid id will not retrieve an
achievement post, check wether a user can update their own post, and a post cannot be updated by someone
who doesn't own it.

![Testing achievements detail view](./assets/documents/tests-achievement-detail.png)

- All tests passed

![Results for achievements detail view](./assets/documents/results-achievements-detail-view.png)

### Memo_posts List View
- Tests to make sure users can retrieve all memo posts, a logged in user can update their
memo posts, and a logged out user cannot create a memo post.

![Testing memo_posts list view](./assets/documents/memo-list-tests.png)

- All tests passed

![Results for memo_posts list view](./assets/documents/memo-list-tests-results.png)

### Memo_posts Detail View
- Tests to check that a valid id will retrieve a memo post, an invalid id will not retrieve a
memo post, check wether a user can update their own post, and a post cannot be updated by someone
who doesn't own it.

![Testing memo_posts detail view](./assets/documents/memo-retrieve-data-tests.png)

![Testing memo_posts detail view 2nd screenshot](./assets/documents/memo-update-tests.png)

- All tests passed

![results for memo_posts detail view](./assets/documents/memo-retrieve-test-results.png)
![Results for memo_posts deatail view 2nd screenshot](./assets/documents/memo-update-results.png)

### Todo List View
- Tests to make sure users can retrieve the Todo list, a logged in user can update their
Todo list, and a logged out user cannot create a Todo list.

![Testing Todo list view](./assets/documents/tests-todo-list.png)

- All test passed

![Results for Todo list view tests](./assets/documents/results-todo-list-test.png)

### Todo Detail View
- Tests to check that a valid id will retrieve a Todo list, an invalid id will not retrieve a
Todo list, check wether a user can update their own Todo list, and a Todo list cannot be updated by someone
who doesn't own it.

![Tests for Todo detail view](./assets/documents/test-todo-detail.png)

- All tests passed

![Results for Todo detail view tests](./assets/documents/results-todo-detail-tests.png)

## Validator Testing
- Files from the project were run through the online pep8 validator, as each one was checked I marked it
off on a table, There were 3 errors, one was found from the validator, which was no new line at the end of the file, the other two was line too long which was corrected before running through the validator.

![Validator table for checking](./assets/documents/p5-pep8-testing-table.png)

![Error found in pep8 validator](./assets/documents/error-pep8-url.png)

## Manual Testing
- Manual Tests were carried out for the Url paths, search and filter functionality, and CRUD functionality, all were made into tables and checked off.

### URL Path tests
![URL path tests table](./assets/documents/p5-testing-paths.png)
![URL path tests for deployed api](./assets/documents/api-url-deployed-check.png)

### Search and Filter testing
![Search and Filter testing](./assets/documents/p5-search-filters-testing-table.png)

### CRUD Testing
- Table was made to check a user could **C**reate, **R**ead, **U**pdate, or **D**elete items.
- The table for deployed was testing in the front link to the front end [here](https://github.com/Mrst12/pp5-frontend-react-appy-families/blob/main/TESTING.md)
- I used a key in the table 
    - LI meaning the user was logged in, and so could Create, and read.
    - LO meaning the user was not logged in and so could only read.
    - LI/O meaning the user was logged in **and** the owner so had full CRUD functionality.

![CRUD table of testing](./assets/documents/p5-crud-testing-table.png)

back to the [README.md](README.md)