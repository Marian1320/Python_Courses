# Write a function that validates a URL string. Handle the ValueError by raising a custom
# exception if the URL format is invalid.Write a function that removes an element at a
# specified index from a list. Handle the IndexError by raising a custom exception if the
# index is out of range.

import re

def validate_url(url):
    url_regex = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'

    if not re.match(url_regex, url):
        raise ValueError(f"Invalid URL format: {url}")
    print(f"Valid URL: {url}")

def remove_element_at_index(my_list, index):
    try:
        removed_element = my_list.pop(index)
        print(f"Removed element: {removed_element}")
    except IndexError:
        raise IndexError(f"Error: Index {index} is out of range.")
try:
    validate_url("https://www.example.com")  # Valid URL
    validate_url("ftp://example.com")  # Valid URL
    validate_url("invalid_url")  # Invalid URL (will raise exception)
except ValueError as e:
    print(e)


my_list = [10, 20, 30, 40, 50]
try:
    remove_element_at_index(my_list, 2)  # Valid index (removes 30)
    remove_element_at_index(my_list, 10)  # Invalid index (will raise exception)
except IndexError as e:
    print(e)
