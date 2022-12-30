# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding gr


number = float(input('number grading system'))

if number >= 80 and number <= 100:
    print('a')
elif number >= 60 and number < 80:
    print('B')
elif number >= 50 and number < 60:
    print('C')
elif number >= 45 and number < 50:
    print('D')
else:
    print('F')
