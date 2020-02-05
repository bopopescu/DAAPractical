# complexity of QuickSort is O(n2)
import mysql.connector
from time import *
def quicksort(rollNo, low , high):
    if low<high:
        pi=partition(rollNo,low,high)
        # Sub array    one - array whose value is less than the pivot
        #              second - array whose values are more the the pivot
        quicksort(rollNo,low,pi-1)
        quicksort(rollNo , pi+1, high)

def partition(rollNo,low ,high):
    # to set the fixed position of pivot in the list
    pivot=rollNo[high]
    i=low-1
    for j in range(low,high):
        if(rollNo[j]<=pivot):
            i+=1
            rollNo[i] , rollNo[j]=rollNo[j],rollNo[i]
    rollNo[i+1], rollNo[high] = rollNo[high], rollNo[i+1]
    return (i+1)


if __name__=="__main__":
    print("Name : Malika Jain\nRoll No: 1706465")
    sql = " select * from Student"
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="DAA")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    list = []
    for row in rows:
        rollno = row[3]
        list.append(rollno)
    print("\nList before Sorting\n ", list)
    n=len(list)
    low=0
    high=n-1
    timestamp1 = time()
    quicksort(list,low,high)
    timestamp2 = time()
    print()
    print("List After  Quick Sort :\n" , list)
    print("Time taken to quick sort is:", timestamp2 - timestamp1)
