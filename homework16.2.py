def show_employee(employee_name, salary=50000):
    print(employee_name, "is the best employee of the month getting bonus", salary)
show_employee("Brandon")

#example with keyword argument
def keyword_argument(first_name, last_name):
    print("Have a wonderful day", first_name,last_name)

keyword_argument(last_name="Pan",first_name="Natalie")

#example with 2 positional argument
def twopositional_argument(first_name, last_name):
    print("Good job", first_name, last_name,"I love our gas prices")
twopositional_argument("Brandon", "Biden")

#example with 1 positional argument
def onepositional_argument(name1):
    print(name1, "is the biggest planet in solar system")
onepositional_argument("Jupiter")