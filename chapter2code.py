"""

    Title:      Chapter 2 Code
    Purpose:    (Knowledge Development) Learning Python in Coursera's Python
                for Everyone Specialization
    Author:     Billy Caughey
    Date:       2019.12.24 - Initial Build

"""

""" Exercise 2.2 """

# The code below almost works

name = input("Enter your name")
print("Hello " + name)

""" Exercise 2.3 """

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate per hour:"))
print(hrs * rate)

""" Exercise 3.1 """

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate per hour:")
r = float(rate)

if h <= 40:
    pay = h * r
    print("Your pay is " + pay)
else:
    h1 = 40
    h2 = h - 40
    pay = h1 * r + h2 * (r * 1.50)
    print("Your pay is " + pay)

print(pay)

""" Exercise 3.3 """

score = float(input("Enter Score:"))

if score > 1.0 or score < 0.0:
    print("Scores must be between 0.0 and 1.0")
    exit
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
