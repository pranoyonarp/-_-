# COMMAND LINE RANDOM PASSWORD GENERATOR
#random password generator
import random
print("enter the length of password you want to generate")
length=int(input())
print("enter the character set you prefer for your password:1 for letters, 2 for numbers, 3 for symbols")
choice=int(input())
password=""
letters="abcdefghijklmnopqrstuvwxyz"
numbers="123456789"
symbols="!@#$%^&*()_-=+[]{}:;,.<>/?~`"
if choice==1:
    for i in range(length):     
        password=password+random.choice(letters)
    print(password)
elif choice==2:
    for i in range(length):     
        password=password+random.choice(numbers)
    print(password)
elif choice==3:
    for i in range(length):     
        password=password+random.choice(symbols)
    print(password)
