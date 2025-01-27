# Write a function that prompts the user to enter a number and tries to convert it to an
# integer. Handle the TypeError exception by printing a message indicating that the input
# is not a valid number. Use a finally block to print "Type conversion process completed."

def convert_to_integer():
    try:
        user_input = input()

        user_number = int(user_input)
        print(f"The number is {user_number}.")

    except TypeError:
        print("Error")

    finally:
        print("Type conversion process completed.")


convert_to_integer()
