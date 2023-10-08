import string
import random

def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    print(s)
    
    # passlen =int(input("Enter the length of password "));
    # print("password lenght is",passlen)
    passwrd =("".join(s[0:6]))
    print("Your dummy password is ",passwrd)
    
    
    val =True
    if len(passwrd)<6:
        print("length should be at least 6")
        val =False
        
    if len(passwrd)>20:
        print("length should be at most 20")
        val =False
        
    if not any(char.isdigit() for char in passwrd):
        print('password should have at least on e numerical value')
        val=False
        
    if not any(char.isupper() for char in passwrd):
        print("password should have at least one UpperCase letter")    
        val=False
    
    if not any(char in s4 for char in passwrd):
        print("password should have at least one Special character")    
        val=False
    else:
        print("Congratulations! You have entered a Strong Password")
            
    
gen()    



