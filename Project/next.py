# 1st method
n,k=map(int,input().split())
scr=list(map(int,input().split()))
t=scr[k-1]
count=0
for x in scr:
    if x>=t and x>0:
        count+=1
print(count)
# With modification
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# t = a[k-1]
# ans = sum(1 for x in a if x >= t and x > 0)
# print(ans)