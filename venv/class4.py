import mysql.connector

print("Malika Jain \n1706465\n")

con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="DAA")
cursor = con.cursor()
sql="SELECT * FROM knapsack "
cursor.execute(sql)
list = cursor.fetchall()



print("###########Given Data############\n",list,"\n")
maxWeight=int(input("Enter Maximum Weight of Knapsack = "))

load=0
totalValue=0
knapsack=[]

print("\n*********Criteria1************")

sql1="SELECT * FROM knapsack ORDER BY Value DESC"
cursor.execute(sql1)
list1 = cursor.fetchall()

for i in range(0, len(list1)):
    load+=list1[i][2]
    if load<=maxWeight:
        knapsack.append(list1[i][0])
        totalValue+=list1[i][1]
        knapsackWeight=load
print("Items in the Knapsack = ",knapsack)
print("Total Weight in the Knapsack = ",knapsackWeight)
print("Total value of the Knapsack = ", totalValue)

load=0
totalValue=0
knapsack=[]

print("\n*********Criteria2************")

sql2="SELECT * FROM knapsack ORDER BY WEIGHT ASC"
cursor.execute(sql2)
list2 = cursor.fetchall()
for i in range(0, len(list2)):
    load+=list2[i][2]
    if load<=maxWeight:
        knapsack.append(list2[i][0])
        totalValue+=list2[i][1]
        knapsackWeight=load
print("Items in the Knapsack = ",knapsack)
print("Total Weight in the Knapsack = ",knapsackWeight)
print("Total value of the Knapsack = ", totalValue)

load=0
totalValue=0
knapsack=[]
count=0

print("\n*********Criteria3************")


finalList=[]
for i in range(0,len(list)):
    innerlist=[]
    for j in range(0,3):
        innerlist.append(list[i][j])
    finalList.append(innerlist)
    profit=finalList[i][1]/finalList[i][2]
    finalList[i].append(profit)

finalList.sort(key = lambda x: x[3],reverse=True)

for i in range(0, len(finalList)):
    load+=finalList[i][2]
    if load<=maxWeight:
        knapsack.append(finalList[i][0])
        totalValue+=finalList[i][1]
        knapsackWeight=load
        count+=1
leftWeight=maxWeight-knapsackWeight
if leftWeight>0:
    value=finalList[count][3]*leftWeight
    knapsack.append(finalList[count][0])
    totalValue+=value
    knapsackWeight+=leftWeight
print("Items in the Knapsack = ",knapsack)
print("Total Weight in the Knapsack = ",knapsackWeight)
print("Total value of the Knapsack = ", totalValue)


