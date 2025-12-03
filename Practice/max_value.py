def maximum(array):
    print(array)
    max=array[0]
    print(max)
    for num in array:
        if num>max:
            max=num
    return max        

print("Enter the size:")
n=int(input())
arr=[]
for x in range(n):
    num=int(input())
    arr.append(num)   
maximum_value=maximum(arr)
print("The maximum value is ",maximum_value)