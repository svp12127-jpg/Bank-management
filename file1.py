#file 1
import csv,os
#create
def create(user,password,name,acc_no,late):
    #checking type of account
    f=open("file 1.csv","a",newline="")
    w=csv.writer(f)
    print("""
Our bank offers these types of accounts.
Savings Account
Current Account
Joint Account
Salary Account
Business Account
Student Account
""")
    type=input("Please enter the type of account you want:")
    if type.lower()=="joint account":
        n=int(input("Please enter number of additional co-owners:"))
        for i in range(n):
            joint_name=input("Please enter name of co-owner:")
            name=name+" "+joint_name
            
    #checking limiting balance amount
    while True:
        balance=eval(input("Please enter amount to be deposited into the bank:"))
        if balance<2000:
            print("Amount deposited is too low.")
            #print("too low to create an account")
            print("Please deposit more than 2000 to your bank account.")
        else:
            break
    l=[user,password,name,acc_no,type,balance,late]
    w.writerow(l)
    f.close()
def delete(user):
    choice=input("To successfully delete your account, please enter yes:")
    if choice.upper()=="YES":
        f=open("file 1.csv","r")
        f1=open("filek.csv","w",newline="")
        r=csv.reader(f)
        w=csv.writer(f1)
        for i in r:
            if i[0]==user:
                pass
            else:
                w.writerow(i)
        f.close()
        f1.close()
        os.remove("file 1.csv")
        os.rename("filek.csv","file 1.csv")
        print("""Deletion process: You can ask for cash, a bank cheque or transfer to a different account
Please visit us in person for final procedures.
Thank you for choosing our bank.""")
#delete("dummy2")
#displaying account balance
def displaybalnc(user):
    f=open("file 1.csv","r")
    r=csv.reader(f)
    for i in r:
        if i[0]==user:
            i[5]=round(float(i[5]),2)
            print("Your account balance is",i[5])
    f.close()

