import pymysql as p
import stdiomask
C=p.connect(host="localhost",password="Zawna@123",user="root",database="Library")
Cur=C.cursor()
sp=' '*3
ln="-"*113

def check(BCODE , Table):
    Cur.execute(f"Select BCODE from {Table} where BCODE = {BCODE}")
    if Cur.fetchone()==None:
        return False
    return True

def Display():
    Cur.execute("Select * from Books")
    Content=Cur.fetchall()
    print(ln)
    print(f"{'BCODE':5}{sp}{'BNAME':^55}{sp}{'AUTHOR':^40}{sp}{'QTY':^3}{sp}")
    print(ln)
    for i in Content:
        print(f"{i[0]:5}{sp}{i[1]:^55}{sp}{i[2]:^40}{sp}{i[3]:^3}{sp}")
    print(ln)

def Issue():
    print(ln)
    BCODE=int(input("Enter the Book Code which you want to get issued :- "))
    if check(BCODE,'Books'):
        Cur.execute(f"Select QTY from Books where BCODE = {BCODE}")
        Count=Cur.fetchone()
        for i in Count:
            if i==0:
                print("Book Out of Stock!")
                break
        else:
            BID=int(input("Enter User ID (Must be an Integer) :- "))
            NAME=input("Enter Name :- ")
            DD=int(input("Enter today's Day :- "))
            MM=int(input("Enter the Month :- "))
            YY=int(input("Enter the Year (20XX) :- "))
            Date=f"{YY}-{MM}-{DD}"
            if DD>24 and MM in (1,3,5,7,8,10,12):
                if MM==12:
                    ReturnDate=f"{YY+1}-1-{DD-24}"
                else:
                    ReturnDate=f"{YY}-{MM+1}-{DD-24}"
            elif DD>23 and MM in (4,6,9,11):
                ReturnDate=f"{YY}-{MM+1}-{DD-23}"
            elif DD>21 and MM==2:
                if YY%4==0 and YY%400==0 and YY%100!=0:
                    ReturnDate=f"{YY}-{MM+1}-{DD-22}"
                else:
                    ReturnDate=f"{YY}-{MM+1}-{DD-21}"
            else:
                ReturnDate=f"{YY}-{MM}-{DD+7}"
            Cur.execute(f"Insert into users values({BID},'{NAME}',{BCODE},'{Date}','{ReturnDate}')")
            Cur.execute(f"Update books set QTY = QTY-1 where BCODE={BCODE}")
            C.commit()
            print(f"Book Issued! \nYou must Return the Book By :- '{ReturnDate}'")
    else:
        print("Book Not Available!")
    print(ln)

def Return():
    print(ln)
    BCODE=int(input("Enter Book Code to be returned :- "))
    BID=int(input("Enter User ID :- "))
    Cur.execute(f"Select BCODE,BID from Users where BCODE={BCODE} and BID={BID}")
    if Cur.fetchone()!=None:
        Cur.execute(f"Update Books set QTY=QTY+1 where BCODE={BCODE}")
        C.commit()
        Cur.execute(f"Delete from Users where BCODE={BCODE} and BID={BID}")
        C.commit()
        print("Book Returned Successfully!")
    else:
        print("No such User Present!")
    print(ln)

#ADMIN OPTIONS ⛔

def Add(N):
    for i in range(N):
        print(ln)
        print(f"Fill in the Necesasary Details of Book {i+1} ")
        BCODE=int(input("Enter Book Code :- "))
        if check(BCODE,'Books')==True:
            print("Book Already Exists")
            print(ln)
            break
        BNAME=input("Enter Book Name :- ")
        AUTHOR=input("Enter Author's Name :- ")
        QTY=int(input("Quantity :- "))
        Cur.execute(f"Insert into Books values({BCODE},'{BNAME}','{AUTHOR}',{QTY})")
        C.commit()
        print("Book(s) added Successfully!")
        print(ln)      

def Remove():
    print(ln)
    BCODE=int(input("Enter Book Code to be removed :- "))
    if check(BCODE,'Books')==True:
        Cur.execute(f"Delete from Books where BCODE={BCODE}")
        C.commit()
        print("Boook Removed Successfully!")
    else:
        print("Book does not Exist!")
    print(ln)

def Modify():
    print(ln)
    BCODE=int(input("Enter Book Code to be Modified :- "))
    if check(BCODE,'Books'):
        while True:
            print(ln)
            print("Modification Options:- \n1)Book Name \n2)Author Name \n3)Quantity \n4)Exit")
            Ch=int(input("Choose from 1 to 4 :- "))
            if Ch==1:
                BookName=input("Enter Modified Name :- ")
                Cur.execute(f"Update Books set BNAME='{BookName}' where BCODE={BCODE}")
                C.commit()
                print(ln)
            elif Ch==2:
                AuthorName=input("Enter Modified Name :- ")
                Cur.execute(f"Update Books set AUTHOR='{AuthorName}' where BCODE={BCODE}")
                C.commit()
                print(ln)
            elif Ch==3:
                Quantity=int(input("Enter New Quantity :- "))
                Cur.execute(f"Update Books set QTY={Quantity} where BCODE={BCODE}")
                C.commit()
                print(ln)
            elif Ch==4:
                print(ln)
                break
            else:
                print("Wrong Option Selected!")

def UserDisplay():
    Cur.execute("Select * from Users")
    Content=Cur.fetchall()
    Ln="-"*70
    print(Ln)
    print(f"{'BID':^5}{sp}{'NAME':^20}{sp}{'BCODE':^5}{sp}{'ISSUING DATE':^10}{sp}{'RETURN DATE':^10}")
    print(Ln)
    for i in Content:
        print(f"{i[0]:^5}{sp}{i[1]:^20}{sp}{i[2]:^5}{sp}{str(i[3]):^10}{sp}{str(i[4]):^10}")
    print(Ln)

def Search(UN):
    Fobj=open("/Users/jain.nabhi966/Desktop/Python Project/Database.txt","r")
    L=Fobj.readlines()
    D={}
    for I in L:
        Rec=I.split() 
        D[Rec[0]]=Rec[1]
    if UN in D:
        return 1
    return 0

def Register():
    UserName=input("Create Username : ")
    X=Search(UserName)
    if X==1:
        print("UserName already exists...")
        Register()
    Pass=input("Create Password : ")
    CPass=input("Confirm Password : ")
    if Pass!=CPass:
        print("Passwords don't match ,\nPlease Re-enter your Credentials")
        print(ln)
        Register()
    else:
        if len(Pass)<5:
            print("Password is too short , \nTry Again!")
            print(ln)
            Register()
        else:
            Fobj=open("/Users/jain.nabhi966/Desktop/Python Project/Database.txt","a")
            Fobj.write(f"{UserName} {Pass}\n")
            print("Registered Successfully!\nLogin to Continue")
            Fobj.close()
            print(ln)
            Login()
            

def Login():
    Fobj=open("/Users/jain.nabhi966/Desktop/Python Project/Database.txt","r")
    UserName=input("Enter Username : ")
    Pass=stdiomask.getpass(prompt="Enter Password: ")
    L=Fobj.readlines()
    D={}
    Rec=[]
    for I in L:
        Rec=I.split() 
        D[Rec[0]]=Rec[1]
    if UserName in D:
        if D[UserName]==Pass:
            print(ln)
            print(f"Login Successful... \nHello {UserName}")
            print(ln)
            pass
        else: 
            print("Password Incorrect...\nTry Again!")
            print(ln)
            Login()
    else:
        print("Sign-up before Logging in...\nTry Again")
        print(ln)
        Register()

#MENU 📊📈

print("LOGIN AS : \n1.USER \n2.ADMIN\n")
Ch=int(input("Enter 1 or 2 : "))
if Ch==1:
    while 1:
        print("USER OPTIONS : \n1.SHOW BOOKS \n2.ISSUE BOOK \n3.RETURN BOOK \n4.EXIT")
        Ch2=int(input("Choose from 1 to 4 : "))
        if Ch2==1:
            Display()
        elif Ch2==2:
            Issue()
        elif Ch2==3:
            Return()
        elif Ch2==4:
            print("Thank You for using our Library Management System....")
            print(ln)
            break
        else:
            print("Wrong Choice....")

elif Ch==2:
    print("1.LOGIN \n2.SIGN-UP")
    Choice=int(input("Enter 1 or 2 : "))
    if Choice==1:
        Login()
    elif Choice==2:
        Register()
    else:
        print("Wrong Choice...")
    while 1:
        print("ADMIN OPTIONS : \n1.SHOW BOOKS \n2.ADD BOOK(s) \n3.REMOVE BOOK \n4.SHOW USERS \n5.MODIFY \n6.EXIT")
        Ch2=int(input("Choose from 1 to 6 : "))
        if Ch2==1:
            Display()
        elif Ch2==2:
            NOB=int(input("Enter the number of Books to be added :- "))
            Add(NOB)
        elif Ch2==3:
            Remove()
        elif Ch2==4:
            UserDisplay()
        elif Ch2==5:
            Modify()
        elif Ch2==6:
            print("Logging Out...")
            print(ln)
            break        
        else:
            print("Wrong Choice....")