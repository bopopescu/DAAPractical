print("Mohit Sharma- 1706476")

def subset_sum(arr,k,total=0,subset=[]):

    if total == k:
        return True
    
    elif len(arr) < 1 or total > k:
        return False

    for i,item in enumerate(arr):
        total += item
        subset.append(item)
        index = len(subset) - 1
        if subset_sum(arr[:i]+arr[i+1:], k, total,subset):
            return True
        total -= item
        subset.pop(index)

arr = [2,9,10,1,99,3]
k = 8
subset = []

if subset_sum(arr,k,0,subset):
    print ('Required subset :',subset)

else:
    print ('No solution exists')