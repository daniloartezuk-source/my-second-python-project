day = int(input())
month = int(input())
year = int(input())

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if month in (1, 3, 5, 7, 8, 10, 12):
    days_in_month = 31
elif month in (4, 6, 9, 11):
    days_in_month = 30
else:
    days_in_month = 29 if is_leap else 28

day += 1

if day > days_in_month:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1

print(f"{day}.{month}.{year}")