# 1----------------------------------

day = input("What day is it? ")
print("Today is", "Monday." if day.lower() == "monday" else "not Monday.")
print("Today is", "not a weekday." if day.lower() == 'saturday' or day.lower() == 'friday' else "a weekday.")

weekly_hours = 1060
hourly_rate = 379
weekly_paycheck = ((weekly_hours - 40) * (hourly_rate * 1.5)) + (40 * hourly_rate)

# 2-----------------------------------

i = 5
while i <= 15:
    print(i)
    i += 1

x = 100
while x >= -10:
    print(x)
    x -= 5

'''y = 2
while y < 1000000:
    print(y ** 2)
    y += 1'''

z = 100
while z >= 5:
    print(z)
    z -= 5

num  = int(input("Pick a number:"))

if isinstance(num, int):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Invalid entry")

for i in range(1, 10):
    print(f"{i}" * i)

odd_num = input("Enter an odd number between 1 and 50:")
while not (odd_num.isdigit() and int(odd_num) >= 1 and int(odd_num) <= 50 and (int(odd_num) % 2 != 0)):
    odd_num = input("Invalid input. Enter an odd number between 1 and 50:")
print(f"Number to skip is: {odd_num}\n")
for count in range(1, 51):
    if count == int(odd_num):
        print(f"Yikes! Skipping number: {odd_num}")
    elif count % 2 != 0:
        print(f"Here is an odd number: {count}")
    else:
        continue

pos_num = input("Enter a positive number:")
if pos_num.isdigit() and int(pos_num) > 0:
    for x in range(0, int(pos_num)):
        print(x)

pos_num = input("Enter a positive number:")
if pos_num.isdigit() and int(pos_num) > 0:
    for x in range(int(pos_num), 0, -1):
        print(x)

# 3------------------------------------

nums = [x for x in range(1, 101)]

for num in nums:
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 4 ----------------------------------

con_ = True
while con_ == True:
    num2 = input("What number would you like to go up to?")

    print("Here is  your table!\n")
    print(" number | squared | cubed ")
    print(" ------ | ------- | ----- ")
    for num in range(1, int(num2) + 1):
        print(" {} | {} | {} ".format(num, num ** 2, num ** 3))

    if input("Would you like to continue?") == 'Y'.lower():
        con_ = True
    else:
        con_ = False

# 5 ----------------------------------

cont_ = True
while cont_ == True:
    score = int(input("Enter a grade:"))
    if 100 >= score >= 90:
        print("A")
    elif 90 > score >= 80:
        print("B")
    elif 80 > score >= 70:
        print("C")
    elif 70 > score >= 60:
        print("D")
    elif score < 60:
        print("F")

    if input("Would you like to continue?") == 'y'.lower():
        cont_ = True
    else:
        cont_ = False

# 6 -----------------------

books = [{"title": "Gulliver's Travels", "author": "Jonathon Swift", "genre": "Adventure"},
        {"title": "Fahrenheit 451", "author": "Ray Bradbury", "genre": "Sci-Fi"},
        {"title": "The Shining", "author": "Stephen King", "genre": "Horror"}]

#for book in books:
#    print(book)

genre = input("Enter a genre:").lower()
for book in books:
    if book["genre"].lower() == genre:
        print(book)