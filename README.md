# Edwin's Password Checker

Edwin's Password Checker is a Python-based web application that allows users to securely check if their passwords have been compromised in any known data breaches. The app uses the Have I Been Pwned API to perform the check and provides a user-friendly interface for easy password submission.

## Features
Secure password checking using the Have I Been Pwned API
Simple and user-friendly web interface
Responsive design for mobile devices
Flask back-end to handle API requests

 ## Prerequisites
Before you can run the password checker application, ensure that you have the following software installed on your machine:
* Python 3.7 or later
* Pip (Python package manager)

## Acknowledgments
* Pwned Passwords API for providing the password data
* Flask for enabling easy web application development
* Axios for simplifying AJAX requests in the web interface

Installation
1. Clone the repository:

`git clone https://github.com/yourusername/password-checker.git`

2. Navigate to the project directory:

`cd password-checker`

3. Create a virtual environment:

`python -m venv venv`

4. Activate the virtual environment:

* On Windows:

`venv\Scripts\activate`

* On macOS or Linux:

`source venv/bin/activate`

5. Install the required Python packages:

`pip install -r requirements.txt`

## Usage

1. Start the Flask development server:

`python app.py`

2. Open your web browser and navigate to the following address:

`http://127.0.0.1:5000/`

3. Enter your password in the provided input field and click the "Check" button.

4. The application will display the result, indicating whether your password has been compromised and, if so, how many times it has been found in known data breaches.
