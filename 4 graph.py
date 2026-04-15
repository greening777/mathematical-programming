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
            

# graph = graphM(5)
# graph.add_edge_un(0,1)
# graph.add_edge_un(1,3)
# graph.add_edge_un(2,0)
# graph.add_edge_un(2,1)
# graph.add_edge_un(2,3)
# graph.add_edge_un(3,2)
# graph.add_edge_un(3,4)
# graph.print_graph()

# graph.dfs_mat(0)
# print("")

graph=graphM(9)
graph.add_edge_un(0,1)
graph.add_edge_un(0,3)
graph.add_edge_un(1,2)
graph.add_edge_un(2,5)
graph.add_edge_un(3,4)
graph.add_edge_un(3,6)
graph.add_edge_un(4,7)
graph.add_edge_un(5,8)
graph.add_edge_un(6,7)
graph.dfs_mat(0)
print("")
graph.bfs_mat(0)

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
                    
        
    
    
# al=graphL(5)
# al.add_edge_un(0,1)
# al.add_edge_un(1,3)
# al.add_edge_un(2,0)
# al.add_edge_un(2,1)
# al.add_edge_un(2,3)
# al.add_edge_un(3,4)
# print(al.ad)

# visited=[0]*5
# al.dfs_list(0, visited)
# print("")



al=graphL(9)
al.add_edge_un(0,1)
al.add_edge_un(0,3)
al.add_edge_un(1,2)
al.add_edge_un(2,5)
al.add_edge_un(3,4)
al.add_edge_un(3,6)
al.add_edge_un(4,7)
al.add_edge_un(5,8)
al.add_edge_un(6,7)
print("")
print(al.ad)
visited=[0]*9