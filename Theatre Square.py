import math
n,m,a=map(int,input().split())

length=math.ceil(n/a)
width=math.ceil(m/a)

total=length*width
print(total)