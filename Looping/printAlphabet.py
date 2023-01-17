# start = 1
# end = 128
# increment = 1
#
# # a = 97
#
# for i in range(start, end + 1, increment):
#     print(chr(i), end=" ")
#


# i = 2
#
# while i <= 100:
#     print(i, end=' ')
#     i = i+2


n = int(input("Enter:"))

start = 1
end = 10
increment = 1

for i in range(start, end + 1, increment):
    print(i, 'x', n, '=', i * n)
