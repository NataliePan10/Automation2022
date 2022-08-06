#exercise 1
clothes = ["socks", "shirt", "skirt", "scarf"]
def insert_element(new_cloth, index=0):
    clothes.insert(index, new_cloth)
insert_element('hat',1)
print(clothes)

insert_element('dress', -1)
print(clothes)


insert_element('blouse')
print(clothes)

insert_element('red', -2)
print(clothes)

#Exercise 2
employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
def replace_employee( old_employee, new_employee, index=0):
    new_list = employee_shift.replace("Mike", "Natalie")

print(new_list)














