# A school has the following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade


number = float(input('number grading system'))

if 80 <= number <= 100:
    print('a')
elif 60 <= number < 80:
    print('B')
elif 50 <= number < 60:
    print('C')
elif 45 <= number < 50:
    print('D')
else:
    print('F')
