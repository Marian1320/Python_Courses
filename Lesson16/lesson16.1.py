# Write a function that checks the length of a string provided by the user. Handle the
# TypeError by raising a custom exception if the input is not a string.
from logging import exception


def check_string_length(user_input):
    try:
        if not isinstance(user_input, str):
            raise exception ("Input is not a string!")
        return len(user_input)

    except exception as e:
        print(f"Error: {e}")
        return None

print(check_string_length("Hello World"))