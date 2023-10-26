# COMMAND LINE RANDOM PASSWORD GENERATOR
import random
print("enter the length of password you want to generate")
length=int(input())
print("enter the character set you prefer for your password")
choice=int(input())
password=""
if choice==1:
    listof_letters="abcdefghijklmnopqrstuvwxyz"
    for i in range(length):     
        password=password+random.choice(listof_letters)
    print(password)
elif choice==2:
    listof_letters="123456789"
    for i in range(length):     
        password=password+random.choice(listof_letters)
    print(password)
elif choice==3:
    listof_letters="!@#$%^&*()_-=+[]{}:;,.<>/?~`"
    for i in range(length):     
        password=password+random.choice(listof_letters)
    print(password)
elif choice==4:
    listof_letters="abcdefghijklmnopqrstuvwxyz123456789"
    for i in range(length):     
        password=password+random.choice(listof_letters)
    print(password)
elif choice==5:
    listof_letters="abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-=+[]{}:;,.<>/?~`"
    for i in range(length):     
        password=password+random.choice(listof_letters)
    print(password)
elif choice==6:
    listof_letters="123456789!@#$%^&*()_-=+[]{}:;,.<>/?~`"
    for i in range(length):     
        password=password+random.choice(listof_letters)
    print(password)
elif choice==7:
    listof_letters="abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_-=+[]{}:;,.<>/?~`"
    for i in range(length):     
        password=password+random.choice(listof_letters)
    print(password)
