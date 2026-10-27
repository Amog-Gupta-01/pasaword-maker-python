lazy import secrets
lazy import getpass
lazy import json

valt={}

def generation():
    password=""
    char=list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890~!@#$%^&*")
    length=int(input("how long you want your password to be?\n-->".title()))
    for _ in range(0,length):
        digi=secrets.choice(char)
        password+=digi
    return password

def search():
     if valt=={}:
         print("you haven't saved any password!!")
     else:
         web=input("which website's password do you want?\n-->").lower()
         if web in valt:
             return f"your password is {valt.get(web)}"
         else:
             return f"No such account found!!"

def delete():
     if valt=={}:
            print("you haven't saved any password!!")
     else:
         delete_name=input("which website's password do you want to remove\n-->").lower()
         if delete_name in valt:
            valt.pop(delete_name)
            return f"we have sucessfully deleted {delete_name}'s password"
         else:
             return f"No such account found!!"

def displaying():
    if valt=={}:
        print("you haven't saved any password!!")
    else:
        for web1 in valt.items():
            print(f"your all websites name are--->")
            return f"{web1}"

def security():
    print("enter the master password!")
    user2= getpass.getpass("--->")
    if user2==master_pass:
        return True
    else:
        return False

print("first create a master password!!")
master_pass=getpass.getpass("--->")

while True:

    print(''' ---------------what do you want to do--------------

    1.add a password
    2.search for a password
    3.delete a password
    4.desplay all password
    5.exit''')

    user1=input("-->")
    
    if user1=="1":
        name=input("for which website you are making password\n-->").lower()
        password1= generation()
        valt[name]=password1
     
    elif user1=="2":
        if security()==True:
            b=search()
            print(b)
        else:
            print("your password was incorrect!!")
            continue   

    elif user1=="3":
        if security()==True:
           c=delete()
           print(c)
        else:
            print("your password was incorrect!!")
            continue   

    elif user1=="4":
        if security()==True:
           d= displaying()
           print(d)  
        else:
            print("your password was incorrect!!")
            continue 
        
    elif user1=="5":
        with open ("vault.txt","w") as vault:
            json.dump(valt,vault,indent=4)
        break

    else:
        print("invalid command!!")