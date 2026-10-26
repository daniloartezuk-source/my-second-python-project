n = int(input())

tens = n // 10  
ones = n % 10   

if tens > ones:
    print(1)
elif tens < ones:
    print(2)
else:
    print("=")