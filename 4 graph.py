####인접행렬 그래프


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
            

graph = graphM(5)
graph.add_edge_un(0,1)
graph.add_edge_un(1,3)
graph.add_edge_un(2,0)
graph.add_edge_un(2,1)
graph.add_edge_un(2,3)
graph.add_edge_un(3,2)
graph.add_edge_un(3,4)
graph.print_graph()

graph.dfs_graph(0)
print("")

######리스트 사용 그래프

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

al=graphL(5)
al.add_edge_un(0,1)
al.add_edge_un(1,3)
al.add_edge_un(2,0)
al.add_edge_un(2,1)
al.add_edge_un(2,3)
al.add_edge_un(3,4)
print(al.ad)

visited=[0]*5
al.dfs_list(0, visited)
print("")



