# Urban Grocers 

## Objective

To validate the Urban Grocers API kit creation endpoint (POST /api/v1/kits/) by developing an automated Pytest suite in Python, ensuring strict parameter validation and API contract compliance.

## Defining the problem

In the Urban Grocers platform, creating product kits relies on strict backend input validation to maintain data integrity. Allowing malformed payload structures, out-of-range character lengths, unhandled spaces, or incorrect data types into the database can disrupt inventory management and cause client-side application crashes.
The endpoint (POST /api/v1/kits/) required thorough validation against 9 specific checklist scenarios—covering both positive cases (expecting an HTTP 201 Created response) and negative/edge cases (expecting an HTTP 400 Bad Request error). Automating these scenarios with Python, Pytest, and Requests was essential to ensure fast, repeatable validation and prevent regression issues.

## What I Did
- Analyzed API documentation and specifications to identify expected endpoint
- Applied Equivalence Partitioning and Boundary Value Analysis to design efficient positive and negative test cases covering character limits, spaces, special characters, numeric values, missing parameters, and incorrect data types.
- Used Postman to manually construct and execute REST API requests, inspecting JSON request payloads, HTTP response bodies, headers, and status codes before automation.
- Developed an automated API test suite using Python, Pytest, and the Requests library to automate checklist scenarios and validate actual HTTP status codes against business rules.
- Uncovered critical backend edge-case failures (such as returning 201 Created or 500 Internal Server Error instead of 400 Bad Request) and documented application discrepancies with clear evidence.
- Uploaded and managed project source code, test suites, and documentation using Git and GitHub workflows.

## Technologies Used

Postman · Python · Pytest · PyCharm · Git · GitHub · REST API Testing · JSON · Boundary Value Analysis · Equivalence Partitioning · Requests

## Results
- Executed 9 automated test scenarios covering both positive and negative validation paths (5 passed, 4 failed).
  
  Critical API Findings & Defects Identified: 
  - Data Validation Flaws (201 Created instead of 400 Bad Request):* The system incorrectly allowed kit creation for an empty string name, a 512-character string (exceeding maximum limit), and numeric data types (123), indicating missing backend validation rules.
  - Server Error Handling (500 Internal Server Error instead of 400 Bad Request): Omitting the mandatory name parameter caused an unhandled internal server error instead of returning a proper client-error status code.
- Uncovered vulnerabilities that, if left unfixed, would allow invalid data persistence and potentially destabilize database integrity.

## Learnings

- Enhanced skills in API test automation using Python, Pytest, and HTTP response assertion handling.
- Deepened practical experience applying Equivalence Partitioning and Boundary Value Analysis to REST API payloads.
- Learned to organize test code and manage project changes using Git and GitHub.

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
