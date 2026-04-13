class graphM:
    def __init__(self, size):
        self.mat=[[0 for _ in range(size)] for _ in range(size)]
    def add_edge_un(self,src,dst):
        self.mat[src][dst]=1
        self.mat[dst][src]=1
    
    def dfs_graph(self, node, visited=None):
        if visited is None:
            visited=[]
        visited.append(node)
        print(node, end='->')
        for i in range(0, len(self.mat)):
            if self.mat[node][i]==1 and i not in visited:
                self.dfs_graph(i,visited)
            
    
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
            
            
class graphL:
    def __init__(self,size ):
        self.ad=[[] for _ in range(size)]
        
    def add_edge_dir(self, src, dst):
        self.ad[src].append(dst)
        
    def add_edge_un(self, src, dst):
        self.ad[src].append(dst)
        self.ad[dst].append(src)
        
    def dfs_list(self, node, visited):
        visited[node]=1
        print(node, end="->")
        for i in self.ad[node]:
           if visited[i]==0:
               self.dfs_list(i, visited) 


##quiz4

n= int(input())
m= int(input())

L=[[] for _ in range(n+1)]

for i in range(0, m):
    src, dst= map(int, input().split())
    L[src].append(dst)
    L[dst].append(src)

visited=[0]*(n+1)
def dfs_worm(L,node,visited):
    visited[node]=1
    for i in L[node]:
        if visited[i]==0:
            dfs_worm(L,i,visited)

dfs_worm(L,1,visited)
print(sum(visited)-1)
