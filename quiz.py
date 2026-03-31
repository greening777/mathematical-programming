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
n = int(input())
L=list(map(int, input().split()))

f = int(input())
F=list(map(int, input().split()))
    
def lin_search(L,n):
    for i in range(len(L)):
        if L[i]==n:
            return "yes"
    return "no"

for i in F:
    print(lin_search(L,i), end=' ')
    


##############quiz2
L=list(map(int, input().split()))

L.sort()
B=[]
B.append(L[0])
for i in range(1, len(L)):
    
    if L[i]!=L[i-1]:
        B.append(L[i])
        
print(B)


#########
n, k = map(int, input().split())
L=[]
for i in range(n):
    L.append(int(input()))

end=max(L)
start=1
best=0

while start<=end:
    mid=(start+end)>>1
    tmp=0
    for i in L:
        tmp=tmp+(i//mid)
    if tmp>=k:
        best=mid
        start=mid+1
    else:
        end=mid-1
        
print(best)



############quiz test
###quiz1

n=int(input())
L=[]

def find_txt(L,txt):
    for i in range(len(L)):
        if L[i][0]==txt:
            return i
    return -1

for i in range(n):
    a=input()
    idx=find_txt(L,a)
    if idx==-1:
        L.append(a,1)
    else:
        L[idx][1]=L[idx][1]+1

L.sort(key=lambda x: x[1], reverse=True)

ret=L[0][0]

for i in range(1, len(L)):
    if L[i][1]==L[0][1]:
        if ret>L[i][0]:
            ret=L[i][0]
    else:
        break
    
print(ret)

###quiz2
n=int(input())
L=[]

def find_txt(L,txt):
    for i in range(len(L)):
        if L[i][0]==txt:
            return i
    return -1

for i in range(n):
    a=input()
    idx=find_txt(L,a)
    if idx==-1:
        L.append(a,len(a))
L.sort(key=lambda x: (x[1],x[0]))

for i in L:
    print(i[0])

###quiz3
L=list(map(int,input().split()))

L.sort()
ret=[L[0]]
for i in range(1, len(L)):
    if L[i]!=L[i-1]:
        ret.append(L[i])
ret=ret[::-1]
print(*ret)

###quiz4
L=list(map(int,input().split()))
n=int(input())

L.sort()

def bsearch_h(L,n):
    start=0
    end=len(L)-1
    high = -1
    while start<=end:
        mid=(start+end)>>1
        if L[mid]>n:
            end=mid-1
        elif L[mid]<n:
            start=mid+1
        else:
            high=mid
            start=mid+1
    return high

def bsearch_l(L,n):
    start=0
    end=len(L)-1
    low = -1
    while start<=end:
        mid=(start+end)>>1
        if L[mid]>n:
            end=mid-1
        elif L[mid]<n:
            start=mid+1
        else:
            low=mid
            end=mid-11
    return low

hidx=print(bsearch_h(L,n))
lidx=print(bsearch_l(L,n))

if hidx==-1 or lidx==-1:
    print("None")
else:
    print(lidx,hidx)