import csv
def register():
    data=open("login.csv","w")
    wo=csv.writer(data)
    wo.writerow(["email","Password"])
    email=input("Please Enter Your Email:")
    password=input("Please Enter Your Password:")
    password2=input("Please Confirm Your Password:")
    if password==password2:
        data.write(email+","+password+"\n")
        print("Registration is Succesful...")
    else:
        print("Please Try Again")
    data.close()
def login():
    data=open("login.csv","r") 
    email=input("Please Enter Your Email:")
    password=input("Please Enter Your Password:")
    ro=csv.reader(data) 
    for row in ro:
        if row==[email,password]:
            print("You Are Logged In..")
            return True
    print("Try Again Please")
    return False
register()
login()

