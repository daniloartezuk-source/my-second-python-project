
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a >= c + 1 and b >= d + 1) or (a >= d + 1 and b >= c + 1):
    print("Yes")
else:
    print("No")

