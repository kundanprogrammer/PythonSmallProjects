import string


passwrd =input("Enter the password :")
def password_check(passwrd):
    SpecialPunc = string.punctuation
    # print(SpecialPunc)
    val =True
    if len(passwrd)<6:
        print("length should be at least 6")
        val =False
        
    if len(passwrd)>20:
        print("length should be at most 20")
        val =False
        
    if not any(char.isdigit() for char in passwrd):
        print('password should have at least on e numerical value')
        value=False
        
    if not any(char.isupper() for char in passwrd):
        print("password should have at least one UpperCase letter")    
        value=False
    
    if not any(char in SpecialPunc for char in passwrd):
        print("password should have at least one Special character")    
        value=False
    else:
        print("Congratulations! You have entered a Strong Password")
            
        
            
password_check(passwrd)    