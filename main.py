#main.py
print("----------------------------------------------------------------------------")
print("Welcome to DVR Bank!")
print("To begin,")
print("Please Login or Signup:")
s=None #s is name of credit card taken
import file1,file2,file4,file3,csv,random,sql
while True:
    try:
        print("""Please press
    1 to Login
    2 to Sign Up""")
        print()
        choice=int(input("Enter your choice:"))
#if client does not input a digit
    except:
        print("Please enter either 1 or 2 to move ahead.")
        print()
        continue
#login page
    if choice==1:
        f=open("file 1.csv","r")
        r=csv.reader(f)
        print("---------------------------*****************************-------------------------------------")
        print("To start your journey with us,")
        user=input("Please enter your username:")
        for i in r:
            if user==i[0]:
                while True:
                    passw=input("Please enter your password:")
                    if passw!=i[1]:
                        print("""Wrong Password
Please try again""")
                        continue
                    else:
                        name=i[2]
                        acc_no=i[3]
                        break
                f.close()
                break
        else:
            print("Your account does not exist. Please sign up or recheck your username.")
            continue
        break
#sign up page
    elif choice==2:
        f=open("file 1.csv","r")
        r=csv.reader(f)
        print("--------------------------------------------------------------------------------------------------")
        print("Welcome to our Online Banking portal, developed by Divya, Rishika and Srivaishnavi.")
        print("To unlock multiple benefits like stress-free transactions and easy access into your account,first...")
        user=input("Please create a username: ")
        flag="green"
        for i in r:
            if user==i[0]:
                print("""Username already exists...please try another username or Login to your account""")
                flag="red"
                break
        if flag=="red":
            continue
        print("To create a strong password and ensure high security, please follow the below guidlines:")
        print("""1. At least 8 characters
2. Should have numbers
3. Should have special characters
4. Should have capital letters""")
        passw=input("Please create your password:")
        acc_no=random.randint(1000000000,9999999999)
        name=input("Please enter your full name:")
        late=0
        f.close()
        break
    else:
        print("Please press either 1 or 2 to move ahead.")
        continue
#personal account page

if choice==2:
    file1.create(user,passw,name,acc_no,late)  
#menu
############
print()
print()
print("----------------------------------------------------------------------------------------------------------------")
print("It is a great day today! Welcome to our Online Banking Portal!",name)
print("We offer a wide range of facilities through this portal, and to choose between them you can press:")
while True:
    print("-------------------------------------------------------------------------------------------------------------")
    print("""Press 1,Transfer Money
Press 2,Loan
Press 3,Check Balance
Press 4,Credit Card Offers
Press 5,Notifications
Press 6,Customer Reviews
Press 7,Delete Account
Press 8,Exit""")
    print("-------------------------------------------------------------------------------------------------------------")
############
    ch=int(input("Please enter your choice:"))
#transferring money
    if ch==1:
        print("-------------------------------Our Online Transaction Portal--------------------------------------------")
        print("Send money instantly from your account to any other account in our bank.")
        t=file2.transferring(user)
        file4.addsendnote(t[0],"SENDER",user,t[1])
        file4.addsendnote(t[0],"Receiver",t[1],user)
#loans
    elif ch==2:
        while True:
            print("---------------------------Our Online Loan Portal---------------------------------------------------")
            print("Need a personal loan or considering buying a car? We can make it happen. Discover our extensive range of loan options")
            print("""Press 1, Take loan
Press 2, Pay loan
Press 3, Exit""")
            c=input("Please enter your choice:")
            if c=="1":
                l=file3.takeloan(user)
                file2.bankloan(l,user)
            elif c=="2":
                l=file3.payloan(user)
                file2.payinginstal(l,user)
            elif c=="3":
                break
            else:
                print("Please enter a valid number")
                continue
            break
#checking balance amount
    elif ch==3:
        print()
        print("----------------------------Account Balance-----------------------------------------------------")
        file1.displaybalnc(user)
        print("If you feel that there are any discrepancies in your balance, feel free to contact our In-Person office in xyz street")
        print()     
#credit card offers
    elif ch==4:
        
        s=file4.creditcardoffers(name,acc_no)
        
#notifications
    elif ch==5:
         print("""------------------------Notifications------------------------------------------------""")
         while True:
             print("""Press 1, to view your transaction history
Press 2, to view loan history
Press 3, to view credit card status
Press 4, to exit""")
             c=int(input("Enter your choice:"))
             if c==1:
                 while True:
                         try:
                             file4.f4print(user)
                             break
                         except FileNotFoundError:
                            print("You have not made a transaction yet.")
                            break
                 continue
             elif c==2:
                while True:
                        #acc=int(input("To view your previous loans, please enter your account number:"))
                        try:
                            k=user+"loan"
                            file4.f4print(k)
                            break
                        except FileNotFoundError:
                            print("You have not taken a loan yet.")
                            break
                continue
             elif c==3:
                 print(file4.creditapprove(acc_no))
                 
             elif c==4:
                print("Thank you for using the Notifications Center")
                break
             else:
                print("Please enter a valid number")
                continue
#customer help service provided
    elif ch==6:
        print("--------------------------------------Customer reviews---------------------------------------------")
        print("Our current rating is")
        sql.overallreviews()
        while True:
            print("""Press 1, to add a review
Press 2, to read a review
Press 3, to exit""")
            choice=eval(input("Enter your choice:"))
            if choice==1:
                sql.insert(user,name)
            elif choice==2:
                sql.readrev()
            elif choice==3:
                print("Exiting review page\nThank you for visiting.")
                break
            else:
                print("Please choose again")
    elif ch==7:
        print("Deleting your Account")
        file1.delete(user)
        break
        #used to exit from the website
    elif ch==8:
        print("Thank you for using DVR's online banking portal!")
        break
#if incorrect value is inputted
    else:
        print("Please enter a valid number")
        continue

"""
more than 1 loan and card"""

        
            
