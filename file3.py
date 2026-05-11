import csv,os,creditscore,file4
from datetime import date
income=0
def takeloan(name):
    print("Taking loan")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    f3=open("loan.csv","a",newline='')
    w=csv.writer(f3)
    y=str(date.today()) #Recording date of borrowing loan

    #Entering details
    
    print("""We offer many types of loans:
Personal Loans: For travel or emergencies.
Mortgage Loans: Stable monthly payments with a fixed interest rate.
Auto Loans: Purchasing new or used vehicles.
Student Loans: Educational expenses, including federal and private loans.
Business Loans: Startups and existing businesses.
Construction Loans: Building homes or commercial properties.""")
    print("--------------------------------------------------------------------------------------------------------------------")

    type=input("What type of loan would you like?")
    co=input("What is your collateral?")
    global income
    income=eval(input("What is your yearly income?"))

    print("--------------------------------------------------------------------------------------------------------------------")
    print()

    payments=0
    f2=open("file 1.csv","r")
    r=csv.reader(f2)
    for i in r:
        if i[0]==name:
            acc_no=name
            x=int(i[-1])
            cred=creditscore.creditscores(income,x)
            
    #Checking credits and giving loans accordingly
    if cred>=700:
        print("Your credit score is excellent!")
            
        while True:
            print("Your eligible for loan of atmost 2000000")
            p=eval(input("Enter amount below 2000000")) 
            if p <=2000000: 
                while True:
                    print("---Our offers---")
                    print()
                    print("""1. Interest=3% Time=3 Years
2. Interest= 5% Time=4 Years
3. Interest = 7% Time= 6 Years""") #Offers (Vary according to credit scores)
                    print("Compounded annually")
                    opt=eval(input("Enter choice"))
                    if opt==1:
                        r=3/100
                        t=3
                    elif opt==2:
                        r=5/100
                        t=4
                    elif opt==3:
                        r=7/100
                        t=6
                    else:
                        print("Please try again")
                        continue
            
                    instal = p * r * (1 + r)**t / ((1 + r)**t - 1)
                    print("For each installment pay:",round(instal,2))
                    total=instal*t
                    total=round(total,2)
                    print("Your total installments are:",total)
                    w.writerow([y,name,p,type,co,cred,r,t,total,payments])
                    file4.loantable(acc_no,name,type,y,payments)
                    return p
                    
            else:
                print("Invalid amount. Please try again.") #Amount exceeds limit
                continue
            break
         
    elif cred>=550 and cred<700:
        print("Your credit score is good")
        while True:
            print("Your eligible for loan of atmost 1000000")
            p=eval(input("Enter amount below 1000000"))
            if p<=1000000:
                while True:
                    print("---Our offers---")
                    print()
                    print("""1. Interest=8% Time=6 Years
2. Interest= 9% Time=7 Years
3. Interest = 10% Time= 8 Years""")
                    opt=eval(input("Enter choice"))
                    if opt==1:
                        r=8/100
                        t=6
                    elif opt==2:
                        r=9/100
                        t=7
                    elif opt==3:
                        r=10/100
                        t=8
                    else:
                        print("Please try again")
                        continue
                    
                    instal = p * r * (1 + r)**t / ((1 + r)**t - 1)
                    print("For each installment pay:",round(instal,2))
                    total=instal*t
                    total=round(total,2)
                    print("Your total installments are:",total)
                    w.writerow([y,name,p,type,co,cred,r,t,total,payments])
                    file4.loantable(acc_no,name,type,y,payments)
                    return p
            else:
                print("Invalid amount. Please try again.")
                continue
            break
         
    elif cred>=400 and cred<550:
        print("Your credit score is fair")
        while True:
            print("Your eligible for loan of atmost 500000")
            p=eval(input("Enter amount below 500000"))
            if p<=500000:
                while True:
                    print("---Our offers---")
                    print()
                    print("""1. Interest=13% Time=8 Years
2. Interest= 14% Time=9 Years
3. Interest = 15% Time= 10 Years""")
                    opt=eval(input("Enter choice"))
                    if opt==1:
                        r=13/100
                        t=8
                    elif opt==2:
                        r=14/100
                        t=9
                    elif opt==3:
                        r=15/100
                        t=10
                    else:
                        print("Please try again")
                        continue
                    
                    instal = p * r * (1 + r)**t / ((1 + r)**t - 1)
                    print("For each installment pay:",round(instal,2))
                    total=instal*t
                    total=round(total,2)
                    print("Your total installments are:",total)
                    w.writerow([y,name,p,type,co,cred,r,t,total,payments])
                    file4.loantable(acc_no,name,type,y,payments)
                    return p
            else:
                print("Invalid amount. Please try again.")
                continue
            break
        
    else:
        print("Needs improvement\nSorry no loan") #Very low credit score
        return 0
    print("-----------------------------------------------------------------------------------------------------------------------------")
    
def payloan(na):
    print("Paying loan")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print()
    f3=open("loan.csv","r") 
    r=csv.reader(f3)
    current=str(date.today())
    
    f5=open("pay.csv","w",newline="") #Updating payments
    w=csv.writer(f5)
    
    for i in r:
        if na==i[1]: #Matching usernames
            acc_no=na
            type=i[3]
            
            
            t=int(i[-3]) #Time period
            print(t,"Installments")#Number of installments
            y=i[0]#Date of loan taken initally
            
            p=int(i[2])#Loan taken
            r=float(i[-4])#Rate
            instal = p * r * (1 + r)**t / ((1 + r)**t - 1)
            print("For each installment pay:",round(instal,2))

                            
            i[-1]=int(i[-1])+1
            payment=int(i[-1])
            w.writerow(i)
                
            p=int(i[2])
            r=float(i[-4])
            while True:
                x=input("Please enter Yes to proceed")
                if x.upper()=="YES":
                    print ("Payment successful") #Payment complete
                    
                    #next
                    if y[5:]==current[5:]: #Matching dates
                        print("loan paid on time")#Payment done on time
                        file4.loantable(acc_no,na,type,y,payment)
                    else:
                        f2=open("file 1.csv","r")
                        f2_=open("def.csv","w",newline="")
                        r1=csv.reader(f2)
                        w=csv.writer(f2_)
                        for i in r1:
                            if i[0]==na:
                                i[-1]=int(i[-1])+1 #late variable
                                w.writerow(i)
                            else:
                                w.writerow(i)
                        f2.close()
                        f2_.close()
                        os.remove("file 1.csv")
                        os.rename("def.csv","file 1.csv")
                        file4.loantable(acc_no,na,type,y,payment)
                        print("Your payment was done late") #Payment late
                    #f3=open("loan.csv","r")
                    
                    if payment<t:
                        year=int(current[:4])+payment+1
                        next=str(year)+y[4:]
                        print("Your next Payment",payment+1," is on",next) #Informing details about next payment
                    elif payment==t: #Last payment
                        print("Payments complete! You have paid off your loan")
                        file4.loantable(acc_no,na,type,y,payment)
                        
                    else:
                        print("You have paid off your loan!")
                    
                elif x.upper()=="NO":
                    break
                else:
                    print("Please enter again or enter no to exit")
                    continue
                break
            break
        else:
            w.writerow(i)
        
    else:
        print("No account") #Account not present
    print("-----------------------------------------------------------------------------------------------------------------------------")
    f5.close()
    f3.close()
    os.remove("loan.csv")
    os.rename("pay.csv","loan.csv")
    return instal
#Interface
##while True:
##    print("""1. Take loan
##2. Pay loan""")
##    c=input("Enter choice")
##    if c=="1":
##        takeloan()
##    elif c=="2":
##        payloan()
##    else:
##        print("choose again")
##        continue
##    break
