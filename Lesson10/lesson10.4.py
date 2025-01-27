# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.


import random
num_to_guess = random.randint(1, 100)

while True:
    num = int(input())
    if num>num_to_guess:
        print("it is high")
    elif num<num_to_guess:
        print("it is low")
    else:
        print("it is right")
        break