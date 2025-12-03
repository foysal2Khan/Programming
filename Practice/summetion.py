def Input(num):
    array=[]
    for x in range(num):
        no=int(input())
        array.append(no)
    return array    
def summetion(arr1):
    sum=0
    for x in arr1:
        sum+=x
    return sum    

print("Enter the no:")
n=int(input())
arr=Input(n)
print("The sum of the no's are",summetion(arr))