
def introTutorial(V, arr):
    for i in range(len(arr)):
        if arr[i] == V:
            res = i
    return res

#Counting Sort 1
def countingSort(arr):
    maxx = max(arr)
    countArray = [0]*(maxx+1)
    res = []
    for i in arr:
        countArray[i] += 1

    counter = 0
    for i in range(len(countArray)):
        for _ in range(countArray[i]):
            arr[counter] = i
            counter += 1
    return arr



if __name__ == '__main__':
    result = countingSort([2,2,2,0,0,1,2,2,3,5])
    print(result)