from datetime import date
import pickle,csv
def addsendnote(diff,s,user,user_2):
    file=str(user)+".txt"
    f4=open(file,"a")
    #diff=int(moneyaftr)-int(moneybefr)
    today=date.today()
    
    if s.upper()=="SENDER":
        am="Amount Sent: "+str(diff)+"\n"
        reci="Money Sent to: "+user_2+"\n"
        d="Date of Transaction: "+str(today)+"\n"
        l="--------------------------------------------------------------------------------------\n"
        k=[am,reci,d,l]
        f4.writelines(k)
    elif s.upper()=="RECEIVER":
        am="Amount Received: "+str(diff)+"\n"
        reci="Money Sent By: "+user_2+"\n"
        d="Date of Transaction: "+str(today)+"\n"
        l="--------------------------------------------------------------------------------------\n"
        k=[am,reci,d,l]
        f4.writelines(k)
    f4.close()

def f4print(user):
    file=str(user)+".txt"
    f4=open(file,"r")
    for i in f4.readlines():
        print(i)
    f4.close()


def creditcardoffers(name,acc):
    f=open("credits.dat","ab")
    print("------------------------------------Credit Card Portal-----------------------------")
    while True:
        print("""To know more about our card offers, enter 1
To Apply for a credit card, enter 2
To exit, enter 3""")
        choice=eval(input("Please enter your choice here:"))
        if choice==1:
            print("""These are our exciting credit card offers, each curated especially for you,
1. **Platinum Rewards Card**
   - **Annual Fee:** $99
   - **APR:** 15.99%
   - **Benefits:** 
     - 2% cashback on all purchases
     - Travel insurance
     - Airport lounge access

2. **Gold Cash Back Card**
   - **Annual Fee:** $75
   - **APR:** 18.99%
   - **Benefits:** 
     - 3% cashback on groceries and dining
     - 1% cashback on all other purchases
     - No foreign transaction fees

3. **Student Starter Card**
   - **Annual Fee:** $0
   - **APR:** 19.99%
   - **Benefits:** 
     - 1% cashback on all purchases
     - No annual fee
     - Credit-building tools

4. **Business Advantage Card**
   - **Annual Fee:** $125
   - **APR:** 14.99%
   - **Benefits:** 
     - 5% cashback on office supplies
     - 3% cashback on travel
     - 1% cashback on all other purchases
     - Employee cards at no additional cost

5. **Travel Elite Card**
   - **Annual Fee:** $199
   - **APR:** 16.99%
   - **Benefits:** 
     - 3x points on travel and dining
     - 1x points on all other purchases
     - Complimentary travel insurance
     - Concierge service

6. **Air Miles Explorer Card**
   - **Annual Fee:** $120
   - **APR:** 17.99%
   - **Benefits:** 
     - 3x air miles on travel purchases
     - 1x air mile on all other purchases
     - Complimentary travel insurance
     - Access to exclusive travel deals and discounts\n \n \n
""")
        if choice==2:
            print("""\nYou can apply for a Credit Card if you:
-have a DVR Account
-are aged between 21 and 65
-live in the UAE
-Have an income of Dhs 5000 or greater.\n\n""")
            print("""\nOur available Credit Cards are:
Platinum Rewards Card
Gold Cash Back Card
Student Starter Card
Business Advantage Card
Travel Elite Card
Air Miles Explorer Card\n\n""")
            while True:
                card=input("Enter name of credit card you would like to choose:")
                list=["platinum rewards card","gold cash back card","student starter card","business advantage card","travel elite card","air miles explorer card"]
                if card.lower() not in list:
                    print("Please enter your choice again, Suggestions: Make sure that all words are spelled correctly and there are no unnessecary spaces.")
                    continue
                else:
                    print("""\nTo apply for a credit card, you will need to submit:
=>All proofs of ID, including your:

-passport
-Emirates ID
-residence visa if you're a non-GCC national

=>Proof you're a UAE resident. Choose one of the following:
-a tenancy agreement or EJARI
-title deeds if you’re a homeowner
-a utility bill no more than 2 months old

=>All proofs of income, including:
-the last 2 bank statements from the account your salary is paid into, or 2 salary credits into your DVR account
-a salary certificate from your employer issued in the last month

=>If you're applying for an additional card, you'll also need to provide the passport and Emirates ID information for the additional cardholder.
\n
""")
                    
                    d={}
                    d['name']=name
                    d["acc"]=acc
                    d["card"]=card
                    pickle.dump(d,f)
                    print("You have been registered to apply for the",choice,".Please visit our In-Person Location to submit the requiered documents and later recieve your card, if you recieve a mail approval to do so.")
                    print()
                    break
                f.close()
        if choice==3:
            
            print("Thank you for using DVR's Credit Card Portal, feel free to look at more amazing credit card offers")
            break
    return card
"""
def creditapprove(user,card):
   
    f2=open("file 1.csv","r")
    r=csv.reader(f2)
    line=0
    #acc=int(input("Please enter your account number:"))
    for i in r:
        if line!=0:
            if (i[0])==user:
                late=int(i[-1])
                if late>5:
                    print("Your",card,"is Not Approved")    
                else:
                    print("Your",card,"is Approved")
                break
        line+=1
    else:
        print("You have not taken a credit card yet")
"""
def viewcredits():
    f=open("credits.dat","rb")
    try:
        while True:
            d=pickle.load(f)
            print(d)
    except  EOFError:
        f.close()

def creditapprove(acc):
    f=open("credits.dat","rb")
    f2=open("file 1.csv","r")
    flag="rr"
    k=""
    try:
        while True:
            d=pickle.load(f)
            
            if d["acc"]==acc:
                card=d["card"]
                flag="g"
                break
    except EOFError:
        f.close()
    if flag=="rr":
        s="Your have not applied for a credit card yet\nPlease apply for one from our credit card portal."
        return s 
    r=csv.reader(f2)
    line=0
    for i in r:
        if line!=0:
            if i[3]==str(acc):
                late=int(i[-1])
                if late>5:
                    k= "\nYour "+card+" is Not Approved\n"
                else:
                    k= "\nYour "+card+" is Approved\n"
        line+=1
    f.close()
    f2.close()
    return k
        
def loantable(accno,name,ltype,accdate,inst):
    file=str(accno)+"loan.txt"
    f4=open(file,"a")
    today=date.today()
   
    s=""
    if inst==0:
        loanname="Type of Loan:"+ltype+"\n"
        datetaken="Loan taken on:"+str(accdate)+"\n"
        l="--------------------------------------------------------------------------------------\n"
        k=[loanname,datetaken,l]
        
        f4.writelines(k)
    else:
        k="Installment Paid: "+str(inst)+"\n"
        d="Date Paid: "+str(today)+"\n--------------------------------------------------------------------------------------\n"
        l=[k,d]
        if accdate[-1:-6]==str(today)[-1:-6]:
            
            f4.writelines(l)
        else:
            s="The loan has been paid late."
            l.append(s)
            f4.writelines(l)

