import csv,os
from datetime import date
#transferring
def transferring(user1):

    # Get user input
    x = float(input("Please enter the amount to be transferred: "))
    user2 = input("Enter the receiver's username: ")

    file_path = "file 1.csv"
    temp_path = "nfile 1.csv"

    # Open the original file in read mode and a temporary file in write mode
    with open(file_path, "r") as f, open(temp_path, "a", newline="") as f1:
        reader = csv.reader(f)
        writer = csv.writer(f1)
        line = 0
        transaction_completed = False

        # First loop to deduct from sender's account
        for row in reader:
            if line == 0:
                # Write the header row
                writer.writerow(row)
            else:
                if row[0] == user1:
                    if x <= float(row[5]):
                        row[5] = float(row[5]) - x
                        transaction_completed = True
                        print("Transaction has successfully been completed")
                    else:
                        print("Your transaction has been rejected")
                        print("Please check your balance or contact our call center for any clarifications.")
                writer.writerow(row)
            line += 1
    
    # If transaction completed, update receiver's balance
    if transaction_completed:
        os.remove(file_path)
        os.rename(temp_path, file_path)
        with open(file_path, "r") as f, open(temp_path, "w", newline="") as f1:
            reader = csv.reader(f)
            writer = csv.writer(f1)
            line = 0

            for row in reader:
                if line == 0:
                    writer.writerow(row)
                else:
                    if row[0] == user2:
                        row[5] = float(row[5]) + x
                    writer.writerow(row)
                line += 1

    # Replace old file with the updated one
    os.remove(file_path)
    os.rename(temp_path, file_path)

        
    return x,user2
#transferring("divya")
#deposits function
def deposits():
    f=open("file 1.csv","r")
    nf=open("nfile 1.csv","w",newline="")
    w=csv.writer(nf)
    r=csv.reader(f)
    rate=0.01
    t=str(date.today())
    while True:
        for i in r:
            if t[-2::]=="01" and t[-5:-3]=="01":
                for i in r:
                    p=int(i[-1])
                    ints=p*rate
                    p+=ints
                    print(ints,"amount is credited to your account.")
            w.writerow(i)
    nf.close()
    f.close()
    os.remove("file 1.csv")
    os.rename("nfile 1,csv","file 1.csv")
#transferring("dummy2")
def bankloan(loanamt,user):
    f=open("file 1.csv","r")
    nf=open("nfile 1.csv","w",newline="")
    w=csv.writer(nf)
    r=csv.reader(f)
    t=str(date.today())
    line=0
    for i in r:
        if line==0:
           w.writerow(i) 
        else:
            if i[0]==user:
                p=float(i[-2])
                p+=loanamt
                i[-2]=p
                w.writerow(i)
            else:
                w.writerow(i)
        line+=1
    nf.close()
    f.close()
    os.remove("file 1.csv")
    os.rename("nfile 1.csv","file 1.csv")
def payinginstal(loanamt,user):
    f=open("file 1.csv","r")
    nf=open("nfile 1.csv","w",newline="")
    w=csv.writer(nf)
    r=csv.reader(f)
   
    t=str(date.today())
    line=0
    
    for i in r:
        if line==0:
           w.writerow(i) 
        else:
            if i[0]==user:
                p=float(i[-2])
                p-=loanamt
                i[-2]=p
                w.writerow(i)
            else:
                w.writerow(i)
        line+=1
    nf.close()
    f.close()
    os.remove("file 1.csv")
    os.rename("nfile 1.csv","file 1.csv")
#print("""1.transferring money
#2.deposits from the bank""")



