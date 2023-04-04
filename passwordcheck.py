import requests
import hashlib

def request_api_data(query_char):
    """
    Request data from the Pwned Passwords API.

    Sends a GET request to the Pwned Passwords API with the given query character
    and returns the JSON response.

    Args:
        query_char (str): The first 5 characters of the SHA-1 hashed password.

    Returns:
        dict: The JSON response from the API.

    Raises:
        RuntimeError: If the API request returns a non-200 status code.
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    responds = requests.get(url)
    if responds.status_code != 200:
        raise RuntimeError(f'Error fetching: {responds.status_code}, check the api and try again.')
    return responds

def pwned_api_check(password):
    """
    Check if a password has been pwned using the Pwned Passwords API.

    Hashes the given password using SHA-1, and queries the Pwned Passwords API
    to determine if the password has been leaked. Returns the count of leaks
    for the given password.

    Args:
        password (str): The password to check for leaks.

    Returns:
        int: The number of times the password has been leaked.
    """
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(response)

pwned_api_check('123')