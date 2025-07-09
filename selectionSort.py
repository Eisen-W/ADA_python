def selectionSort(arr, size):
    for i in range(size):
        min_idx = i

        for j in range(i+1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [-2, -5, 9, 6, 23, 56, 16, 0]
size  = len(arr)

print("unsorted array:")
print(arr)

selectionSort(arr, size)

print("sorted array")
print(arr)