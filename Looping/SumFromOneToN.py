# for loop:
#
# variable: i
# starting : 1
# ending: 10
#
# range function (start,end+1,increment)
#
# start = 1
# end = 10
# increment = 1
#
# for alamin in range(start, end + 1, increment):
#
#     print(alamin, end="  ")


# 100 - 1 porjonto print
#
# start = 100
# end = 1
# increment = -1
#
# for i in range(start, end - 1, increment):
#     print(i,end=" ")


# task:  100 98 96 94 .......... 0
#
# start=99
# end=1
# increment=-2
# for alamin in range(start,end-1,increment):
#     print(alamin,end="  ")


# 1+2+3+4+5+........+n  most important
#
# 1 2 3 4 5 6
#    0+1=1
#    1+2 = 3
#    3+3 = 6
#    6+4 = 10
#    10 + 5 = 15

# example: n=10 output: 55

n = 5
# print(n*(n+1)*0.5)

start = 1
end = n
increment = 1
sum = 0

for i in range(start, end + 1, increment):
    sum = sum + i

print(sum)





