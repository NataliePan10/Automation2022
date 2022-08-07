list1 = []
for e in range(1,4):
    list1.append(e)
    print(e)


total = 0
for e in list1:
    total = total + e
print(total)


def print_sum_avg(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg

print("The average is", print_sum_avg([1,2,3]))

def print_sum_avg_ars(*args):
    return sum(args, 0.0) / len(args)
print (print_sum_avg_ars(1, 2, 3))



