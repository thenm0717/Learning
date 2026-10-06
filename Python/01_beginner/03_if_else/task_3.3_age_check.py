"""
Write a program that determines whether or not a user is allowed access to a website.
"""

user_age = int(input('Enter your age: '))

if user_age >= 18:
    print('Access allowed')
else:
    print('Access denied')