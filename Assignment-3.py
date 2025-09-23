# Task 1

def factorial (n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

while True:
    user = int(input("Enter the number: "))
    if user < 0:
        print('Enter Positive number.')
    else:
        ff = factorial(user)
        print("The factorial of",user,'is',ff)
        break



# Task 2 

import math

user2 = int(input(" Enter the number: "))
sq = math.sqrt(user2)
log = math.log(user2)
sine =math.sin(user2)

print(f" Square root: {sq}\n Logarithm: {log}\n Sine: {sine}" )