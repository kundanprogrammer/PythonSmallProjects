# import getpass
# database ={"kundanp0001@gmail.com":"kundan@786","luckypawar1997@gmail.com":"kundan~!@#","amarraj":"191271ar","davcsdept@gmail.com":"asdf!@#$","abc":"def"}
# username = input("Enter the username: ")
# password =getpass.getpass("Enter Your Password: ")
# for i in database.keys():
#     if username ==i:
#         # while password != database.get(i):
        
#             password =getpass.getpass("Enter Your Password Again: ")
        
#         break
    
#     print("verified")    

# print(" NO SUCH USER FOUND: ")    
    
# # if username not in i:
# #     print("No Such User Found")
import getpass
database ={"kundanp0001@gmail.com":"kundan@786","luckypawar1997@gmail.com":"kundan~!@#","amarraj":"191271ar","davcsdept@gmail.com":"asdf!@#$","abc":"def"}
# for i in database:
    # print(database[i])
    
username = input("Enter the username: ")
if username in database.keys():
    password =getpass.getpass("Enter the password: ")
    if password == database[username]:
        print("Congractulations !,Correct Password")
    else:
        i =3
        while(i > 0):
            print("Incorrect Password ,{} attempt left".format(i))
            password =getpass.getpass("Enter the password: ")
            if password == database[username]:
                print("ongractulations !Correct Password")
                break
            else:
                i-=1
            if(i==0):
                print("Enough of attempts: Please Try after 5 mins à")     
                break
      
        
else:
    print("The user is not found , Please Sign In")
    
# print(database.keys())