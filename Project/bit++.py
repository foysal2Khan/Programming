n= int(input())
x=0
for _ in range(n):
    string=str(input().split())
    if "+" in string:
            x+=1
    elif "-" in string:
            x-=1
print(x)