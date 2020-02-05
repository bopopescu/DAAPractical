import mysql.connector
class DBHelper:
    def saveStudentInDB(self,student):
        sql="insert into Student values(null,'{}','{}', '{}', '{}')".format(student.name,student.univ,student.phone,student.email)
        con = mysql.connector.connect(user="root", password="",host="127.0.0.1", database="DAA")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        print("Saved")
    def fetchAllStudentInDB(self):
        # 1. Create SQL Statement
        sql = " select * from Student"

        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="DAA")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        rows= cursor.fetchall()
        list=[]
        for row in rows:
            rollNo= row[2]
            list.append(rollNo)
        print("\n",list)
        print("Total No Of Students : ",len(list))
        choice='yes'
        while (choice=='yes'):
            rollno = int(input("Enter RollNo. of the student  to find"))
            if rollno in list:
                beg=0
                end=len(list)-1
                mid=self.binarySearch(list,beg,end,rollno)
                print(rows[mid])
            else:
                print("wrong Input")
            print()
            print("You want to find details of any other Student(yes/no)")
            choice=input()

    def binarySearch(self, list,beg,end,item):

        while (beg <= end):
            mid = int((beg + end) / 2)
            if (list[mid] == item):
                return  mid
            elif (list[mid] < item):
                beg = mid + 1
                self.binarySearch(list,beg,end,item)
            elif (list[mid] > item):
                end = mid - 1
                self.binarySearch(list,beg,end,item)

class Student:

    def __init__(self, name,univ, phone, email):
        self.name = name
        self.univ=univ
        self.phone = phone
        self.email = email

print("Name : Malika Jain\nRoll No : 1706465")
print()
print("1. Enter Student details in database")
print("2. Show details of a particular Student")
choice=int(input())
if choice==1:
    sRef = Student(None,None,None,None)
    sRef.name = input("Enter Student Name:")
    sRef.univ = input("Enter Student University RollNo:")

    sRef.phone = input("Enter Student Phone:")
    sRef.email = input("Enter Student Email:")


    save = input("Would you like to save Student(yes/no)")
    if save == "yes":
        db = DBHelper()
        db.saveStudentInDB(sRef)
else:
    db=DBHelper()
    db.fetchAllStudentInDB()

