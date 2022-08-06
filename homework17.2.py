
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for abc in xs:
    print(abc)


xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i)

    for i in xs:
        print("the square of", i, "is", i ** 2)
        break

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
for x in range(0,len(xs)):
    total = total + xs[x]
print("Product = ", total)


xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
result = 1
for x in xs:
    result = result * x

print(result)
