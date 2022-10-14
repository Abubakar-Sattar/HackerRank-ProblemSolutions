import os
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food: "))
        if(c==1):
            value=input("Enter which exercise you did and for how much time :\n")
            if (not os.path.exists("exercise.txt")):
                with open("exercise.txt", "w")as f:
                    f.write("0")
            with open("exercise.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Exercise data Stored successfully!!! ")
        elif(c==2):
            value = input("Enter what you had for breakfast, lunch or dinner:\n")
            if (not os.path.exists("food.txt")):
                with open("food.txt", "w")as f:
                    f.write("0")
            with open("food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Food Data Stored successfully !!!")
def retrieve(k):
    if k==2:
        c=int(input("Enter 1 for excersise data and 2 for food data:  "))
        if(c==1):
            print("\nHello ",d,".Here's your exercise data:\n")
            with open("exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            print("\nHello ",d,".Here's your food data:\n")
            with open("food.txt") as op:
                for i in op:
                    print(i, end="")
print("\n\n\t\t\tHealth Management System \n")
d=input(" Enter your name:")
while True:
    a=int(input("\n 1]press 1 for storing your helath status \n 2] for retrieving your data \n 3] Exit application \n "
                "\t Enter your choice : "))
    if a==1:
        take(a)
    elif a==2:
        retrieve(a)
    else:
        exit()
    e=int(input("\n Do you want to add more exercise or food data ??:\n 1] For storing more data press 1 \n 2] For retreving your data press 2 \n 3] To exit application press 3:\n"
                "\t Enter your choice : "))
    if e==1:
        take(e)
    elif e==2:
        retrieve(e)
    else:
         exit()