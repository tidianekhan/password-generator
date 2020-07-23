from __builtin__ import int
import random
import string
#This is an improved version of my earlier password generator which now allows the end user to 
#choose the difficulty of the password they desire. The components used in generating the password
#change depending on the difficulty.
print("This is a random password generator! Input the length and I will generate a password for you!")

passlen = int(raw_input("Choose the length of your password:"))

print("Good! Now input 'E' for an easy password, 'M' for a medium and 'H' for Hard!")

pwd_strength = str(raw_input("Enter your desired password strength: "))

if pwd_strength == 'E':
    password = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for x in range(passlen))
    
elif pwd_strength == 'M':
    password = "".join(random.choice(string.ascii_letters + string.digits) for x in range(passlen))

elif pwd_strength == 'H':
    password = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(passlen))

else:
    print("Invalid input! Try again!")

print(password)