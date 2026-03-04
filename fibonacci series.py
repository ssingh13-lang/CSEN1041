n = int(input())

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#input
5
#output
01123
