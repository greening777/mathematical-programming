
L=list(map(int, input().split()))

L.sort()

R=[]
R.append(L[0])
for i in range(len(L)-1):
    if L[i]!=L[i+1]:
        R.append(L[i+1])
    else:
        pass
        
print(R)