def BubbleSort(lst):
    n=len(lst)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                (lst[j], lst[j+1]) = (lst[j+1], lst[j])
    return lst

x = input("Please input the array: \n")
y = x.split()
arr=[]
for i in y:
    arr.append(int(i))
arr=BubbleSort(arr)
print(arr)



