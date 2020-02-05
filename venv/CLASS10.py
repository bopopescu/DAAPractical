import mysql.connector
import numpy as np

print("Jasmanjot Singh- 1706448")
sql = "SELECT * FROM knapsack "
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="daa")
cursor = con.cursor()
cursor.execute(sql)
data = list(cursor)
cursor.close()
con.close()
w = [i[1] for i in data]
v = [i[2] for i in data]
W = int(input('Enter the capacity of Knapsack: '))


def knapsack_dp(weights, values, W):
    container = np.zeros((len(weights), W + 1), dtype=int)

    for i in range(1, W + 1):
        if weights[0] <= i:
            container[0][i] = values[0]
        else:
            container[0][i] = 0
    for i in range(1, len(weights)):
        for j in range(1, W + 1):
            if weights[i] > j:
                container[i][j] = container[i - 1][j]
            else:
                container[i][j] = max(container[i - 1][j], v[i] + container[i - 1][j - w[i]])

    print('Weights:', weights)
    print('Values:', values)
    print('Maximum Weight of Knapsack:', W)
    print(container)
    print('Maximum value of knapsack = {}'.format(container[-1][-1]))


knapsack_dp(w, v, W)
