# Urban Grocers 

## Objective

To validate the Urban Grocers API and automate test cases for user creation and kit management, ensuring that API requests and responses strictly adhere to business requirements and specifications.

## Defining the problem

The Urban Grocers API required thorough testing to verify that user and kit creation endpoints handled input data correctly. Particular attention was needed for the kit name field under various edge cases—including character limits, special characters, spaces, missing parameters, and invalid data types. Manual execution of these repetitive validation scenarios was time-consuming, highlighting the need for automated tests with Python, PyTest, and Requests to improve testing efficiency and reliability.

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

- 100% of the tests passed. Successfully requested a taxi with the comfort fare in Urban Routes.
- Validated API behavior for user and kit creation, tested positive and negative input scenarios, and identified unexpected behavior in input validation.
- Developed automated tests with Python and Pytest to check API responses against expected results

## Learnings

- Improved my understanding of API requests, responses, and HTTP status codes.
- Practiced applying boundary value analysis and equivalence partitioning to API testing.
- Strengthened my skills in designing positive and negative test scenarios.
- Gained practical experience writing and running automated API tests with Python and Pytest.
- Learned to organize test code and manage project changes using Git and GitHub.

## Evidence

<img width="1096" height="1436" alt="imagen (4)" src="https://github.com/user-attachments/assets/fb5adb01-0fea-4990-a1fa-90c044eeff0e" />


--------------------------------------------------------------------------------

# API Documentation
Located on: Test server(apidoc)/docs/

## How to run the tests
1. Install dependencies: pip install pytest requests

2. Configure the server URL in the configuration.py file

3. Run the tests with pytest
