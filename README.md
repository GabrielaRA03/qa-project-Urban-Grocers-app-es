# Urban Grocers 

## Objective

To validate the Urban Grocers API by automating the test suite for kit creation via the POST method (/api/v1/kits/), ensuring that parameter validation for name adheres strictly to system requirements.

## Defining the problem

Creating a kit in Urban Grocers requires strict input validation for the name parameter to maintain data integrity. The endpoint had to be tested against 9 specific checklist scenarios—covering both valid names (expecting a 201 Created status code) and edge/invalid cases such as special characters, character length limits, spaces, missing parameters, or incorrect data types (expecting a 400 Bad Request status code). Automating these scenarios with Python, PyTest, and Requests was necessary to ensure fast, repeatable validation.

## What I Did

- Analyzed the API documentation and requirements to identify expected behavior.
- Applied Equivalence partitioning and boundary value analysis techniques to design efficient test cases covering both valid and invalid data inputs
- Created checklists and designed positive and negative test cases for API requests.
- Tested user and kit creation endpoints, focusing on the kit name field and its validation rules.
- Verified character limits, spaces, special characters, numeric values, missing parameters, and incorrect data types.
- Used Postman to send API requests and inspect response bodies and HTTP status codes.
- Identified unexpected validation behavior and documented defects with supporting evidence.
- Developed automated API tests using Python and Pytest to validate responses against expected results.
- Uploaded and managed the project code using Git and GitHub.

## Technologies Used

Postman · Python · Pytest · PyCharm · Git · GitHub · REST API Testing · JSON · Boundary Value Analysis · Equivalence Partitioning

## Results

- Validated API behavior for kit creation (POST /api/v1/kits/), executing 9 automated test scenarios:
  - *Positive Tests (1, 2, 5, 6, 7):* Confirmed successful kit creation, receiving an HTTP *201 Created* status code.
  - *Negative Tests (3, 4, 8, 9):* Verified error handling for invalid inputs, returning an HTTP *400 Bad Request* status code as expected.
- Developed automated tests using Python and PyTest to validate API responses against business requirements and identified edge-case input behavior.

## Learnings

- Improved my understanding of API requests, responses, and HTTP status codes.
- Practiced applying boundary value analysis and equivalence partitioning to API testing.
- Strengthened my skills in designing positive and negative test scenarios.
- Gained practical experience writing and running automated API tests with Python and Pytest.
- Learned to organize test code and manage project changes using Git and GitHub.

## Evidence

<img width="1096" height="1436" alt="imagen (4)" src="https://github.com/user-attachments/assets/fb5adb01-0fea-4990-a1fa-90c044eeff0e" />

<img width="1920" height="1011" alt="imagen (5)" src="https://github.com/user-attachments/assets/f7e0b802-baaf-4292-a374-ff28500098bf" />

--------------------------------------------------------------------------------

# API Documentation
Located on: Test server(apidoc)/docs/

## How to run the tests
1. Install dependencies: pip install pytest requests

2. Configure the server URL in the configuration.py file

3. Run the tests with pytest
