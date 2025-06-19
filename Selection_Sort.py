n = int(input("Enter array size: "))
arr = []
print("Enter array elements:")
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    min_pos = i
    for j in range(i+1, n):
        if arr[j] < arr[min_pos]:
            min_pos = j
    arr[i], arr[min_pos] = arr[min_pos], arr[i]

print("Sorted array:", arr)
