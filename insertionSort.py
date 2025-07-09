def insertionSort(arr, size):
    for i in range(1, size):
        key = arr[i]
        j = i-1

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        
        arr[j+1] = key

arr = [3, 5, 13, 9, 6]

print("unsorted array:")
size = len(arr)
print(arr)

insertionSort(arr, size)

print("sorted array")
print(arr)