###########quiz 1

def selection_sort(L):
    for i in range(len(L)):
        idx=i
        for j in range(i+1, len(L)):
            if L[j][1]<L[idx][1]:
                idx=j
            L[i], L[idx] = L[idx], L[i]
    return L

n = int(input())
L=[]
for i in range(n):
    a,b = input().split()
    L.append([a,int(b)])

# selection_sort(L)
L=sorted(L,key=lambda x: x[1])

for i in range(len(L)):
    print(L[i][0], end=' ')
    
#############quiz2
n = int(input())
L=[]
for i in range(n):
    a,b = input().split()
    L.append([int(a),b])

L=sorted(L,key=lambda x: x[0])

    
for i in L:
    print(i[0], i[1])



#######quiz3
n, k = map(int,input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

A.sort()
B.sort()

for i in range(k):
    if A[i]<B[n-1-i]:
        A[i]=B[n-1-i]
    else:
        break

print(A)
print(sum(A))



#########auiz4
n = int(input())
L=[]
for i in range(0, n):
    a = int(input())
    L.append(a)
L.sort(reverse=True)

start=0
end=len(L)-1
total=0


while start<end:
    if L[start]<1 and L[start+1]<1:
        total=total+L[start]*L[start+1]
        start=start+2
        
    else:
        break
    
while end>0:
    if L[end]>1 and L[end-1]>1:
        total=total+L[end]*L[end-1]
        end=end-2
    else:
        break
    
for i in range(start, end+1):
    total=total+L[i]
    
print(total)




#############quiz 1