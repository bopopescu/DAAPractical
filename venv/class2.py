import mysql.connector
from time import *
def merge_sort(sequence):
    """
    Sequence of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(sequence) < 2:
        return sequence

    mid = len(sequence) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_sequence = merge_sort(sequence[:mid])   # element at index mid not included
    right_sequence = merge_sort(sequence[mid:])

    return merge(left_sequence, right_sequence)

def merge(left, right):
    """
    Traverse both sorted sub-arrays (left and right), and populate the result array
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result
print("Name : Malika Jain\nRoll No: 1706465")
sql = " select * from Student"
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="DAA")
cursor = con.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
list = []
for row in rows:
    rollNo = row[3]
    list.append(rollNo)
print("\nList before Sorting \n", list)
print ()
timestamp1=time()
print("List After  Merge Sort :\n",merge_sort(list))
timestamp2=time()
print("Time taken to merge sort is:", timestamp2-timestamp1)
