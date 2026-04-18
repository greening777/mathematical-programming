###quiz_graph


#1
"""
n,k= map(int, input().split())

L=[[] for _ in range(n+1)]
for i in range(k):
    a, b= map(int, input().split())
    L[a].append(b)
    L[b].append(a)

def dfs(L,n,v):
    v[n]=1
    for i in L[n]:
        if v[i]==0:
            dfs(L,i,v)

def dfs_recursive(L):
    v=[0]*len(L)
    cnt=0
    for i in range(1,len(L)):
        if v[i]==0:
            dfs(L,i,v)
            cnt=cnt+1
    return cnt

def dfs_2(L,i,v):
    if v[i]!=0:
        return False
    else:
        v[i]=1
        for n in L[i]:
            dfs(L,n,v)
        return True

def dfs_recursive2(L):
    v=[0]*len(L)
    cnt=0
    for i in range(1, len(L)):
        if dfs_2(L,i,v)==True:
            cnt=cnt+1
    return cnt


def dfs_iter(L):
    v=[0]*len(L)
    cnt=0
    for i in range(1, len(L)):
        if v[i]!=0:
            continue
        cnt=cnt+1
        
        st=[i]
        while st:
            curr=st.pop()
            if v[curr]==0:
                v[curr]=1
                for n in L[curr]:
                    if v[n]==0:
                        st.append(n)
    return cnt

def bfs_chain(L):
    v=[0]*len(L)
    cnt=0
    for i in range(1, len(L)):
        if v[i]!=0:
            continue
        cnt=cnt+1
        v[i]=1
        q=[i]
        
        while q:
            curr=q.pop(0)
            for n in L[curr]:
                if v[n]==0:
                    v[n]=1
                    q.append(n)
    return cnt
                    

print("dfs recursive1 1:", dfs_recursive(L))
print("dfs recursive1 2:", dfs_recursive2(L))
print("dfs iter:", dfs_iter(L))
print("bfs:", bfs_chain(L))


"""


#2
"""
n=int(input())
M=[]

for i in range(n):
    a=list(map(int,input().split()))
    M.append(a)
    
def dfs_mat(M,i,j,v):
    v[i][j]=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for k in range(4):
        x=i + dx[k]
        y= j +dy[k]
        if 0<=x<len(M) and 0<=y<len(M[0]) and v[x][y]==0 and M[x][y]==0:
            dfs_mat(M,x,y,v)

def dfs_mat_recur(M):
    nrow=len(M)
    ncol=len(M[0])
    v=[[0]*ncol for _ in range(nrow)]
    cnt=0
    for i in range(nrow):
        for j in range(ncol):
            if v[i][j]==0 and M[i][j]==0:
                dfs_mat(M,i,j,v)
                cnt=cnt+1
    return cnt

def dfs_mat_iter(M):
    nrow=len(M)
    ncol=len(M[0])
    v=[[0]*ncol for _ in range(nrow)]
    cnt=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(nrow):
        for j in range(ncol):
            if v[i][j]!=0 or M[i][j]==1:
                continue
            cnt=cnt+1
            st=[[i,j]]
            while st:
                curr=st.pop()
                if v[curr[0]][curr[1]]==0:
                    v[curr[0]][curr[1]]=1
                    
                    for k in range(4):
                        x=curr[0]+dx[k]
                        y=curr[1]+dy[k]
                        
                        if 0<=x<nrow and 0<=y<ncol and v[x][y]==0 and M[x][y]==0:
                            st.append([x,y])
    return cnt

def bfs_mat(M):
    nrow=len(M)
    ncol=len(M[0])
    cnt=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    v=[[0]*ncol for _ in range(nrow)]
    
    for i in range(nrow):
        for j in range(ncol):
            if v[i][j]!=0 or M[i][j]==1:
                continue
            
            v[i][j]=1
            q=[[i,j]]
            cnt=cnt+1
            while q:
                curr=q.pop(0)
                
                for k in range(4):
                    x=curr[0]+dx[k]
                    y= curr[1]+dy[k]
                    
                    if 0<=x<nrow and 0<=y<ncol and v[x][y]==0 and M[x][y]==0:
                        v[x][y]=1
                        q.append([x,y])
                        
    return cnt

print("dfs mat recur:", dfs_mat_recur(M))
print("dfs mat iter:", dfs_mat_iter(M))
print("bfs mat:", bfs_mat(M))
"""


###3
"""
n= int(input())
M=[]

for i in range(n):
    a=list(map(int, input().split()))
    M.append(a)
    
def bfs_min_dis(M):
    nrow=len(M)
    ncol=len(M[0])
    v=[[0]*ncol for _ in range(nrow)]
    
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    v[0][0]=1
    q=[[0,0]]
    
    
    while q:
        curr=q.pop(0)
        if curr[0]==nrow-1 and curr[1]==ncol-1:
            return v[curr[0]][curr[1]] -1
        for k in range(4):
            x= curr[0]+dx[k]
            y= curr[1]+dy[k]
            
            if 0<=x<nrow and 0<=y<ncol and v[x][y]==0 and M[x][y]==1:
                v[x][y] = v[curr[0]][curr[1]] + 1
                q.append([x,y])
    return v[nrow-1][ncol-1]

def bfs_min_path(M):
    nrow=len(M)
    ncol=len(M[0])
    v=[[0]*ncol for _ in range(nrow)]
    
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    v[0][0]=1
   
    
    q=[[0,0, [[0,0]]]]
    
    while q:
        i,j,path=q.pop(0)
        
        if i==(nrow-1) and j==(ncol-1):
            return path
        
        for k in range(4):
            x=i+dx[k]
            y=j+dy[k]
            
            if 0<=x<nrow and 0<=y<ncol and v[x][y]==0 and M[x][y]==1:
                v[x][y]=1
                new_p = path+[[x,y]]
                q.append([x,y,new_p])
    return path


print(bfs_min_dis(M))
print(bfs_min_path(M))

"""
###4

n,m=map(int, input().split())
L=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int, input().split())
    L[b].append(a)
    
p=int(input())

def num_book(L,p):
    v=[0]*len(L)
    st=[p]
    
    while st:
        curr=st.pop()
        if v[curr]==0:
            v[curr]=1
            
            for i in L[curr]:
                if v[i]==0:
                    st.append(i)
                    
    return sum(v)-1

print(num_book(L,p))