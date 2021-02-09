def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

x = input("Please input the array: \n")
y = x.split()
arr=[]
for i in y:
    arr.append(int(i))
arr=bubbleSort(arr)
print(arr)


