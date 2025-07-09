def bubbleSort(arr, size):
    for n in range(size -1, 0, -1):
        swapped = False

        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        if not swapped:
            break

arr = [34, 56, 12, 76, 21]
size = len(arr)
print("sorted array:")
print(arr)

bubbleSort(arr, size)

print("sorted array")
print(arr)