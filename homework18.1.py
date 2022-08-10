import random

random_number = random.randint(0, 50)
for attempt in range(7):
    user_input = int(input("Guess the number from 0 to 50:"))
    if user_input < random_number:
        print("The value is too low")
    elif user_input > random_number:
        print("The value is too high")
    elif user_input == random_number:
        print("You guessed correctly")
        break

