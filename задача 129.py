books = int(input())

if books < 2:
    print("You earned 0 points.")
elif 2 <= books < 4:
    print("You earned 5 points.")
elif 4 <= books < 6:
    print("You earned 15 points.")
elif 6 <= books < 8:
    print("You earned 30 points.")
else:
    print("You earned 60 points.")
    