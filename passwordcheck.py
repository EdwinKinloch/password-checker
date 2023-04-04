import requests
import hashlib
import sys
import getpass

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

def get_password_leaks_count(hashes, hash_to_check):
    """
    Count the number of times a password hash appears in the provided hashes.

    This function takes a response from the Pwned Passwords API containing hashes
    and their corresponding leak counts, and checks if the given hash is present
    in the response. If found, it returns the count of leaks for that hash;
    otherwise, it returns 0.

    Args:
        hashes (Response): A requests.Response object containing the API response
                           with hashes and their leak counts.
        hash_to_check (str): The hash of the password to check for leaks.

    Returns:
        int: The number of times the password hash has been leaked.
    """
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

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
    return get_password_leaks_count(response, tail)

def main():
    """
    Check if the given password has been leaked using the Pwned Passwords API.

    The function prompts the user to securely enter a password and checks if
    it has been leaked using the Pwned Passwords API. If the password is found
    in the database, it displays the number of times it has been leaked;
    otherwise, it informs the user that the password was not found.

    Returns:
        str: A message indicating the completion of the process.
    """
    password = getpass.getpass("Enter the password to check: ")
    count = pwned_api_check(password)
    if count:
        print(f'The password was found {count} times... you should probably change your password!')
    else:
        print(f'The password was NOT found.')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main())
