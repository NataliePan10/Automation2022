
number_to_win = 27
user_input = input("Guess the winning number from 20 to 30\n")
while int(user_input) != number_to_win:
    print( "You are wrong! Try one more time!")
    user_input + input("Guess the winning number from 20 to 30\n")
    print(" Not your luck! Try again!")
    user_input = input("Last chance!!!Guess the winning number from 20 to 30\n")

print( " This is a winning number! You are so lucky, its your day!!!")