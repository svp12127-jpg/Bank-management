#sql code to read reviews
import mysql.connector
from datetime import date
obj=mysql.connector.connect(host="localhost",user="root",database="MYFILE",password="Rishika@123")

def readrev():

    c=obj.cursor()
    c.execute("Select * from reviews")
    l=c.fetchall()
    for i in l:
        print("-----------------------------------------")
        print(i[1])
        print(i[-1])
        for j in range(int(i[2])):
            print("★",end=" ")
        for k in range(5-int(i[2])):
            print("☆",end=" ")
        print()
        print(i[3])
    obj.close()
    c.close()
    print("-------------------------------------------------------")
def overallreviews():
    c=obj.cursor()
    c.execute("Select avg(rating) from reviews")
    l=c.fetchall()
    print(l[0][0])
    obj.close()
    c.close()
def insert(x,y):
    #x is username
    #y is name
    c=obj.cursor()
    z=int(input("Enter your rating: "))
    review=input("Enter your review: ")
    d=date.today()
    t=(x,y,z,review,d)
    q="insert into reviews values(%s,%s,%s,%s,%s)"
    c.execute(q,t)
    obj.commit()
    obj.close()
    c.close()
