password = 'kinza'
print('hi alamin.')
user = str(input('ami tomaka khabo:'))
counter = 1

while user != password:
    if counter == 2:
        print('tuy akta banor')

    if counter == 3:
        print('you are date')
        exit(1)

    user = str(input('tomaka khabo'))
    counter = counter + 1

print('hi hi hi hi')
