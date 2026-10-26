n = int(input())
m = int(input())

# Обчислюємо відсоток набраних балів
percent = (n / m) * 100

if percent >= 90:
    print(12)
elif percent >= 70:
    print(8)
elif percent >= 50:
    print(5)
else:
    print(2)