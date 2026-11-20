# Urban Grocers 

## Objective

To test the kit creation endpoint (POST /api/v1/kits/) in Urban Grocers using automated Python and Pytest tests, making sure input rules and API responses work as expected.

## Defining the problem

When users or clients create product kits in Urban Grocers, the backend must check that the data is valid before saving it. If bad data gets through—such as empty names, text that is too long, spaces, wrong data types, or missing fields—it can hurt data quality, create messy records in the inventory, and cause errors in the app.

Testing POST /api/v1/kits/ across 9 checklist cases (valid cases expecting 201 Created, and invalid or edge cases expecting 400 Bad Request) with Python, Pytest and Requests, helps catch problems early, repeat checks quickly, and avoid regressions when the code changes.

## What I Did

- Reviewed the API rules and requirements to understand how kit creation should behave.

- Used Equivalence Partitioning and Boundary Value Analysis to design clear positive and negative test cases for text length limits, spaces, special characters, numbers, missing fields, and wrong data types.

- Tested requests manually in Postman first to inspect JSON bodies, headers, responses, and status codes before automating them.

- Built an automated test suite in Python using Pytest and Requests to run the checklist and check actual status codes against expected rules.

- Found edge-case bugs where the API returned 201 Created or 500 Internal Server Error instead of 400 Bad Request, and documented the findings with clear evidence.

- Saved and organized the code, tests, and documentation using Git and GitHub.


## Technologies Used

Postman · Python · Pytest · PyCharm · Git · GitHub · REST API Testing · JSON · Boundary Value Analysis · Equivalence Partitioning · Requests

## Results & Business Implications

- **Verified test run**: Ran 9 automated test cases covering valid and invalid inputs (5 passed, 4 failed).

- **Invalid data accepted** (201 Created instead of 400 Bad Request): The endpoint allowed creating kits with an empty name (""), a 512-character name (above the limit), and a number (123) as the name.
  - Proven result: 3 failed validation checks
  - possible implication: invalid or inconsistent kit names could enter the database and confuse users or product listings.

- **Server error on missing required field** (500 Internal Server Error instead of 400 Bad Request): Skipping the required name field caused a server error instead of a clean client-error message.
  - Proven result: 1 server-error case
  - possible implication: missing data can trigger unhandled backend errors and make troubleshooting or monitoring harder for the team.
 

## Learnings

- Practiced writing automated API tests with Python, Pytest, and response assertions.

- Applied Equivalence Partitioning and Boundary Value Analysis to real API inputs.

- Practiced keeping test code and project updates organized in Git and GitHub..

## Strategic Recommendations & Product Decision Support

Based on the automated API test results and identified backend vulnerabilities, the following recommendations are critical to ensuring backend robustness and data integrity:

- **Check input types and empty values**: Validate fields on the backend so empty strings and wrong data types (like numbers instead of text) are rejected with 400 Bad Request.
  - Decision support: helps the product team decide whether to block bad inputs right away or adjust validation rules before release.

- **Enforce character length limits**: Make sure the name field strictly follows its allowed length range (such as 1 to 511 characters) instead of accepting over-limit inputs like 512 characters.
  - Decision support: helps prevent display or database issues before release

- **Handle missing required fields cleanly**: Return a clear 400 Bad Request when required fields are missing instead of a 500 Internal Server Error.
  - Decision support: helps product and engineering owners decide if the fix is urgent before launch so real user errors do not look like server crashes.

- **Align API behavior with business rules**: Confirm with product and backend teammates how edge cases should work before shipping so expected behavior matches what users and systems need.

<br>

## Evidence

<img width="1096" height="1436" alt="imagen (4)" src="https://github.com/user-attachments/assets/fb5adb01-0fea-4990-a1fa-90c044eeff0e" />

- Description of the 9 planned checklist scenarios tested against the POST /api/v1/kits/ endpoint, defining the parameter validation rules, expected payloads, and target HTTP status codes (201 Created vs. 400 Bad Request).
  
<br>

####  Automated Test Execution Output

<img width="1920" height="1011" alt="imagen (5)" src="https://github.com/user-attachments/assets/f7e0b802-baaf-4292-a374-ff28500098bf" />

- This evidence shows the Pytest console summary output upon executing the automated test suite, confirming that 5 tests passed as expected while 4 tests failed due to backend validation discrepancies.
 Summary of Failed Automated API Tests

<br><br>

#### Summary of Failed Automated API Tests
 <img width="1500" height="544" alt="WhatsApp Image 2026-10-16 at 6 27 51 PM" src="https://github.com/user-attachments/assets/6951bc14-998c-4d68-9c5d-41afeb7cdf54" />

--------------------------------------------------------------------------------

# API Documentation
Located on: Test server(apidoc)/docs/

## How to run the tests
1. Install dependencies: pip install pytest requests

2. Configure the server URL in the configuration.py file

3. Run the tests with pytest
