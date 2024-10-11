# Python program to demonstrate
# sys.exit()
import sys

age = 17

# program that stops execution if the age is less than 18.
if age < 18:
    # exits the program
    sys.exit("Age less than 18, so exiting")
else:
    print("Age is not less than 18")
