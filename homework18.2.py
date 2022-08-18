
#Exercise #1

user_input = input(" My program will output everything in lowercase until i enter STOP")
while user_input.upper() != "STOP":
        print(user_input.lower())
        user_input = input(" My program will output everything in lowercase until i enter STOP")

#Exercise #2
my_dictionary = {'Jake': '$100K', 'Anand': '$120K'}
for key, value in my_dictionary.items():
    print("The salary of {} is {} K per year".format(key, value))


#Excersise 3

my_tuple = (4, 30, 2017, 2, 27)
print('{}, {}, {}, {}, {}'.format(my_tuple[3], my_tuple[4], my_tuple[2], my_tuple[0], my_tuple[1]))
#2 27 2017 4 30'

