# 1st method
name=input().strip().lower()
name1=set(name)
count=0
for x in name1:
    count+=1

if count%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
# with modification
name=input().strip()
num=len(set(name))
if num%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
