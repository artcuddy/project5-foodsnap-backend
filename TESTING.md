# Testing For API foodSNAP

back to the [README.md](README.md)

## Contents
-   [Automated Unit Testing](#unit-testing)
    -   [foodSNAP List View](#foodsnap-list-view)
    -   [foodSNAP Detail View](#foodsnap-detail-view)
    -   [Recipe Detail View](#recipe-detail-view)
    -   [CommentsDetail View](#comments-detail-view)
    [Validator Testing](#validator-testing)
-   [Manual Testing](#manual-testing)
    -   [URL Path tests](#url-path-tests)
    -   [Search and Filter testing](#search-and-filter-testing)
    -   [CRUD Testing](#crud-testing)

## Automated Unit Testing
- I have used API Testcase to test the views using a red, green refactor method.
### Achievements List View
- Tests to make sure users can retrieve all foodSNAPS, a logged in user can update their
foodSNAPS, and a logged out user cannot create a foodSNAP.

![Testing foodSNAP list view](/documents/readme_images/test-foodsnap-list.webp)

- results all passed
![Results for foodSNAP list view](/documents/readme_images/results-foodsnap-list.webp)


### foodSNAP Detail View
- Tests to check that a valid id will retrieve an foodSNAP, an invalid id will not retrieve an
foodSNAP, check wether a user can update their own post, and a post cannot be updated by someone
who doesn't own it.

![Testing foodSNAP detail view](/documents/readme_images/test-foodsnap-detail.webp)

- All tests passed

![Results for foodSNAP detail view](/documents/readme_images/results-foodsnap-list.webp)

### Recipe Detail View
- Tests to check that a valid id will retrieve a recipe, an invalid id will not retrieve a
recipe, check wether a user can update their own post, and a post cannot be updated by someone
who doesn't own it.

![Testing recipe detail view](/documents/readme_images/test-recipe-detail.webp)


- All tests passed

![results for recipe detail view](/documents/readme_images/results-recipe-detail.webp)

### Comments Detail View
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
- Manual Tests were carried out for the Url paths, search and filter functionality, and CRUD functionality, all were made into tables and checked off.

### URL Path tests
![URL path tests table](./assets/documents/p5-testing-paths.png)
![URL path tests for deployed api](./assets/documents/api-url-deployed-check.png)

### Search and Filter testing
![Search and Filter testing](./assets/documents/p5-search-filters-testing-table.png)

### CRUD Testing
- Table was made to check a user could **C**reate, **R**ead, **U**pdate, or **D**elete items.
- The table for deployed was testing in the front link to the front end [here]()
- I used a key in the table 
    - LI meaning the user was logged in, and so could Create, and read.
    - LO meaning the user was not logged in and so could only read.
    - LI/O meaning the user was logged in **and** the owner so had full CRUD functionality.

![CRUD table of testing](./assets/documents/p5-crud-testing-table.png)

back to the [README.md](README.md)