# take two numbers as input from the user
# example: 12 10
# output: 12 is greater
# 10 is smaller

# 10 10
# output: numbers are equal

a = float(input("Enter first number: "))

b = float(input("Enter second number: "))

# this is a new line

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("numbers are equal")
