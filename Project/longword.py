n=int(input())
for _ in range(n):
    
    word=input().strip()
    
    if len(word)>10:
       first= word[0]
       sec=len(word)-1
       last=word[sec]
       mid=len(word)-2
       print(first+str(mid)+last)
    else:
        print(word)