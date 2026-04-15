####인접행렬 그래프


class graphM:
    def __init__(self, size):
        self.mat=[[0 for _ in range(size)] for _ in range(size)]
        self.size=size
    def add_edge_un(self,src,dst):
        self.mat[src][dst]=1
        self.mat[dst][src]=1
    
    def dfs_mat(self, node, visited=None):
        if visited is None:
            visited=[]
        visited.append(node)
        print(node, end='->')
        for i in range(0, len(self.mat)):
            if self.mat[node][i]==1 and i not in visited:
                self.dfs_mat(i,visited)
            
    def bfs_mat(self,node):
        visited=[0]*self.size
        visited[node]=1
        q=[node]
        while q:
            curr=q.pop(0)
            print(curr, end="->")
            for i in range(0, len(self.mat)):
                if self.mat[curr][i]==1 and visited[i]==0:
                    q.append(i)
                    visited[i]=1
                    
    
    def add_edge_dir(self, src, dst):
        self.mat[src][dst] =1
        
    
    def print_graph(self):
        print(end="  ")
        for i in range(0, len(self.mat)):
            print(i, end=" ")
        print(" ")
        for i in range(0, len(self.mat)):
            print(i, end=" ")
            for j in range(0, len(self.mat)):
                print(self.mat[i][j], end=" ")
            print(" ")
            


######리스트 사용 그래프

class graphL:
    def __init__(self,size ):
        self.ad=[[] for _ in range(size)]
        self.size=size
        
    def add_edge_dir(self, src, dst):
        self.ad[src].append(dst)
        
    def add_edge_un(self, src, dst):
        self.ad[src].append(dst)
        self.ad[dst].append(src)
        
    def dfs_list(self, node, visited): #recursive
        visited[node]=1
        print(node, end="->")
        for i in self.ad[node]:
           if visited[i]==0:
               self.dfs_list(i, visited) 
    def dfs_list_iter(self, node):
        visited=[0]*self.size
        st=[node]
        while st:
            curr=st.pop()
            if visited[curr]==0:
                visited[curr]=1
                print(curr, end="->")
                for i in self.ad[curr]:
                    if visited[i]==0:
                        st.append(i)
        
    
    def bfs_list(self, node):
        visited=[0]*self.size
        visited[node]=1
        q=[node]
        while q:
            curr=q.pop(0)
            print(curr, end="->")
            for i in self.ad[curr]:
                if visited[i]==0:
                    visited[i]=1
                    q.append(i)
                    
        
    



# ##quiz4 - dfs

# n= int(input())
# m= int(input())

# L=[[] for _ in range(n+1)]

# for i in range(0, m):
#     src, dst= map(int, input().split())
#     L[src].append(dst)
#     L[dst].append(src)

# visited=[0]*(n+1)
# def dfs_worm(L,node,visited):
#     visited[node]=1
#     for i in L[node]:
#         if visited[i]==0:
#             dfs_worm(L,i,visited)

# dfs_worm(L,1,visited)
# print(sum(visited)-1)


# ###############bfs
# n= int(input())
# m= int(input())

# L=[[] for _ in range(n+1)]

# for i in range(0, m):
#     src, dst= map(int, input().split())
#     L[src].append(dst)
#     L[dst].append(src)
    
# def bfs_p1(L,start):
#     v=[0]*(n+1)
#     v[start]=1
#     q=[start]
#     while q:
#         curr=q.pop(0)
#         for i in L[curr]:
#             if v[i]==0:
#                 v[i]=1
#                 q.append(i)
#     return sum(v)-1

# print(bfs_p1(L,1))



#####quiz4-2

#bfs
def bfs_s(L,start,target):
    visited=[0]*len(L)
    visited[start]=1
    q=[start]
    dis=[0]*len(L)
    while q:
        curr=q.pop(0)
        if curr==target:
            return dis[curr]
        
        for i in L[curr]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)
                dis[i]=dis[curr]+1
    return -1 

L=[[1, 3], [0, 2], [1, 5], [0, 4, 6], [3, 7], [2, 8], [3, 7], [4, 6], [5]]
print(bfs_s(L,0,4))

#dfs
def dfs_d(L,start,target):
    visited=[0]*len(L)
    dis=[0]*len(L)
    st=[start]
    while st:
        curr=st.pop()
        if visited[curr]==0:
            visited[curr]=1
            
            for i in L[curr]:
                if visited[i]==0:
                    dis[i]=dis[curr]+1
                    st.append(i)
    return dis[target]

print(dfs_d(L,0,2))