# ########1_1

# n=int(input())
# A=[]

# for i in range(n):
#     a=input()
#     if a == "del":
#         if len(A)!=0:
#             A.pop() 
#     else:
#         A.append(int(a))
        
# print(sum(A))



# ########1_2
# n=int(input())
# A=[]
# P=[]

# for i in range(n):
#     a=input().split()
#     if a[0]=="push":
#         A.append(int(a[1]))
#     elif a[0]=="pop":
#         if len(A)==0:
#             P.append(-1)
#         else:
#             P.append(A.pop())
#     elif a[0]=='top':
#         if len(A)==0:
#             P.append(-1)
#         else:
#             P.append(A[-1])
#     elif a[0]=="size":
#         P.append(len(A))



# for i in range(len(P)):
#     print(P[i])




# ########1_3


# class bNode:
#     def __init__(self, data):
#         self.data=data
#         self.left=None
#         self.right=None
#         self.cnt=1
    
# class bstree:
#     def __init__(self):
#         self.root=None
#     def insert(self, data):
#         if self.root is None:
#             self.root=bNode(data)
#         else:  
#             self._insert(self.root, data)
            
#     def get_size(self,node):
#         if node is None:
#             return 0
#         else:
#             return node.cnt
    
#     def _insert(self, node, data): #1<root<r
#         if data<node.data:
#             if node.left is None:
#                 node.left=bNode(data)
#             else:
#                 self._insert(node.left, data)
#         elif data>node.data:
#             if node.right is None:
#                 node.right=bNode(data)
#             else:
#                 self._insert(node.right, data)
#         node.cnt=1+self.get_size(node.left)+self.get_size(node.right)
    
#     def cnt_geq(self, val):
#         if self.root is None:
#             return 0
#         ret=self._cnt_geq(self.root, val)
#         return ret
    
#     def _cnt_geq(self, node, val):
#         if node is not None:
#             if node.data>=val:
#                 rsize = self.get_size(node.right)
#                 return 1+rsize+self._cnt_geq(node.left, val)
#             else:
#                 return self._cnt_geq(node.right, val)
#         else:
#             return 0
#     def print_tree(self):
#         if self.root is None:
#             print("empty tree")
#         else:
#             self._print_tree(self.root,0)
#     def _print_tree(self, node, level):
#         if node is not None:
#             self._print_tree(node.right, level + 1)
#             print(' ' * level + str(node.data))
#             self._print_tree(node.left, level + 1)


# L=list(map(int, input().split()))
# val=int(input())
# bst=bstree()

# ret=[]

# for i in L:
#     bst.insert(i)
#     cnt=bst.cnt_geq(val)
#     ret.append(cnt)

# print(*ret)


# ######4


# n = int(input())
# A = []

# for _ in range(n):
#     a, b = input().split()
#     a = int(a)

#     if a == 0:
#         if len(A) == 0:
#             continue
#         else:
#             A.sort(key=lambda x: (abs(x[0]), x[0]))
#             print(A.pop(0)[1])
#     else:
#         A.append((a, b))
        




class minheap:
    def __init__(self):
        self.heap=[]
    
    def _parent(self,idx):
        #(idx-1)//2
        return (idx-1)>>1
    
    def _left_child(self, idx):
        return (idx*2)+1
    
    def _right_child(self, idx):
        return (idx*2)+2

    ###insert
    def insert(self,dis, menu):
        self.heap.append([abs(dis),dis,menu])
        self._heapify_up(len(self.heap)-1)
        
    def _heapify_up(self, idx):
        pidx=self._parent(idx)
        while idx>0 and self.heap[idx]<self.heap[pidx]:
            self.heap[idx], self.heap[pidx]=self.heap[pidx],self.heap[idx]
            idx=pidx
            pidx=self._parent(idx)
            
        
    ###delete  
    def extract(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()[2]
        
        min_val = self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return min_val[2]
    
    def _heapify_down(self, idx):
        lenh = len(self.heap)
        while True:
            lidx = self._left_child(idx)
            ridx = self._right_child(idx)
            min_idx=idx
            if lidx<lenh and self.heap[lidx]<self.heap[min_idx]:
                min_idx=lidx
            if ridx<lenh and self.heap[ridx]<self.heap[min_idx]:
                min_idx=ridx
            if min_idx ==idx:
                break
            self.heap[min_idx], self.heap[idx]=self.heap[idx], self.heap[min_idx]
            idx=min_idx
            
n=int(input())
L=[]
for i in range(n):
    a, b = input().split()
    L.append([int(a),b])
    
menu=minheap()
for i in L:
    if i[0]!=0:
        menu.insert(i[0], i[1])
    else:
        print(menu.extract())