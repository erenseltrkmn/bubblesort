def swap(array,a,b):
    temp=array[a]
    array[a]=array[b]
    array[b]=temp
    return array



def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr=swap(arr,j,j+1)
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

arr=bubbleSort(arr)
print(arr)
