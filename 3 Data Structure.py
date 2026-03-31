####Data Structure


###linked list(doubly)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class dbllist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def append(self, data):
        newnode=Node(data)
        if self.head:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
            self.size+=1
        else:
            self.head=newnode
            self.tail=newnode
            self.size+=1
    def print_fwd(self):
        curr=self.head
        while curr:
            print(curr.data, end="<->")
            curr=curr.next
        print("None")
    def print_back(self):
        curr=self.tail
        while curr:
            print(curr.data, end="->")
            curr=curr.prev
        print("head")
    def delete(self, data):
        curr=self.head
        while curr:
            if curr.data==data:
                if curr==self.head:
                    self.head=curr.next
                    if curr.next:
                        curr.next.prev = None
                    else: #self.next.none(head=tail)
                        self.tail=None
                elif curr==self.tail:
                    self.tail=curr.prev
                    curr.prev.next=None
                else:
                    curr.prev.next=curr.next
                    curr.next.prev=curr.prev
                self.size-=1
                return
            curr=curr.next
        print("Not found")

    def selection_sort(self):
        curr=self.head
        while curr:
            min_node=curr
            next_node=curr.next
            while next_node:
                if next_node.data<min_node.data:
                    min_node=next_node
                next_node=next_node.next
            curr.data, min_node.data =  min_node.data, curr.data
            curr=curr.next
    def insert_sort(self):
        curr=self.tail.next
        while curr:
            min_node=curr
            prev_node=curr.prev
            next_node=curr.next
            
            while prev_node and prev_node.data>min_node.data:
                prev_node=prev_node.prev
                
            if min_node.prev:
                min_node.prev.next=min_node.next
            if min_node.next:
                min_node.next.prev=min_node.prev
                
            if prev_node is None: #min_node is head
                min_node.next=self.head
                min_node.prev=None
                self.head.prev=min_node
                self.head=min_node
            else: #not head
                min_node.next=prev_node.next
                min_node.prev=prev_node
                if prev_node.next:
                    prev_node.next.prev=min_node
                prev_node.next=min_node
                
            if min_node.next is None:
                self.tail=min_node
                
            curr=next_node  
                
                
###########test#########
# tlist=dbllist()
# tlist.append(4)
# tlist.append(3)
# tlist.print_fwd()
# tlist.print_back()

# tlist=dbllist()
# tlist.append(4)
# tlist.append(2)
# tlist.append(6)
# tlist.append(5)
# tlist.append(1)
# tlist.append(3)
# tlist.append(0)
# tlist.print_fwd()
# tlist.selection_sort()
# print("===selection sort===")
# tlist.print_fwd()




#########stack##########

class stack_array:
    def __init__(self):
        self.stack=[]
    def push(self, data):
        self.stack.append(data)
    def is_empty(self):
        return len(self.stack)==0
    
    def pop(self):
        if self.is_empty()==True:
            print("empty stack")
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty()==True:
            print("empty stack")
        else:
            return self.stack[-1]


class sNode:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class stack_llist:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self, data):
        newnode=sNode(data)
        newnode.next=self.top
        self.top=newnode
        self.size+=1
    def pop(self):
        if self.size==0:
            print("empty stack")
        else:
            data = self.top.data
            self.top=self.top.next
            self.size-=1
            return data
    def print_stack(self):
        curr=self.top
        while curr:
            print(curr.data)
            print("|")
            curr=curr.next  
        print("=========")
        
       
class queue_list:
    def __init__(self):
        self.queue=[]
    def enqueue(self, data):
        self.queue.append(data)
    def is_empty(self):
        return len(self.queue)==0
    def dequeue(self):
        if self.is_empty()==True:
            print("empty queue")
        else:
            return self.queue.pop(0)
       
class queue_llist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def enqueue(self, data):#add to tail
        newnode=sNode(data)
        if self.tail:
            self.tail.next=newnode
            self.tail=newnode
            self.size+=1
        else:
            self.head=newnode
            self.tail=newnode
            self.size+=1
        
    def dequeue(self): #remove from head
        if self.size==0:
            print("empty queue")
        else:
            data=self.head
            if self.head.next:
                self.head.next.prev=None
                self.head=self.head.next
            else:
                self.head
                self.tail=None
            self.size-=1
            return data
    def print_queue(self):
        curr=self.head
        while curr:
            print(curr.data, end="->")
            curr=curr.next
        print("None")
        
        
###########test##########
# slist=stack_array()
# slist.push(1)
# slist.push(2)
# slist.push(3)
# # print(slist.stack)
# # print(slist.pop())
# # print(slist.stack)
# # print(slist.peek())

# slist.print_stack()


# lq=queue_list()
# lq.enqueue(1)
# lq.enqueue(2)
# lq.enqueue(3)
# print(lq.queue)
# print(lq.dequeue())
# print(lq.dequeue())
# print(lq.dequeue())
# print(lq.queue)
# print(lq.dequeue())
        
        
#####n-ary tree#######
class nNode:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.rightsibling=None

def add_child(parent, child):
    if not parent.leftchild:
        parent.leftchild=child
    else:
        curr=parent.leftchild
        while curr.rightsibling:
            curr=curr.rightsibling
        curr.rightsibling=child
        
def print_display(node, level=0):
    if node is None:
        return
    print(" " * level + str(node.data))
    print_display(node.leftchild, level + 1)
    print_display(node.rightsibling, level)

#########test##########
# root=nNode("a")
# c1=nNode("b")
# c2=nNode("c")
# c3=nNode("d")

# add_child(root, c1)
# add_child(root, c2)
# add_child(c1,c3)
# print_display(root)
        

class bNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
class bstree:
    def __init__(self):
        self.root=None
    def insert(self, data):
        if self.root is None:
            self.root=bNode(data)
        else:  
            self._insert(self.root, data)
    def _insert(self, node, data): #1<root<r
        if data<node.data:
            if node.left is None:
                node.left=bNode(data)
            else:
                self._insert(node.left, data)
        elif data>node.data:
            if node.right is None:
                node.right=bNode(data)
            else:
                self._insert(node.right, data)
                
                
    def search(self, data):
        return self._search(self.root, data)
    
    def _search(self, node, data):
        if node is None:
            return 0
        if node.data==data:
            return 1
        elif data<node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)            

    def remove(self, data):
        if self.search(data):
            self._remove(self.root, data)
        else:
            print("Not found")
    def _remove(self, node, data):
        if node is None:
            return node
        
        if data<node.data:
            node.left=self._remove(node.left, data)
            return node
        
        elif data>node.data:
            node.right=self._remove(node.right, data)
            return node
        
        else: #node.data==data
            if node.left is None and node.right is None:
                return None
            elif node.right:
                node.data=self.sucessor(node)
                node.right=self._remove(node.right, node.data)
                return node
            else:
                node.data=self.predecessor(node)
                node.left=self._remove(node.left, node.data)
                return node
    def sucessor(self, node):
        curr=node.right
        while curr.left:
            curr=curr.left
        return curr.data
    def predecessor(self, node):
        curr=node.left
        while curr.right:
            curr=curr.right
        return curr.data
    
    def display_inorder(self):
        if self.root is None:
            print("empty tree")
        else:
            self._display_inorder(self.root)
    
    def _display_inorder(self, node):
        if node is not None:
            self._display_inorder(node.left)
            print(node.data, end="->")
            self._display_inorder(node.right)
    
    def inorder_stact(self):
        if self.root is None:
            print("empty tree")
            return
        curr=self.root
        stack=[]
        ret=[]
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            ret.append(curr.data)
            curr=curr.right
        return ret
    
    # def inorder_stact(self):
    #     if self.root is None:
    #         print("empty tree")
    #         return
    #     curr=self.root
    #     stack=[]
    #     stackdata=[]
    #     ret=[]
    #     while curr or stack:
    #         while curr:
    #             stack.append(curr)
    #             stackdata.append(curr.data)
    #             curr=curr.left
    #             print("stact", stackdata)
    #         curr=stack.pop()
    #         pd=stackdata.pop()
    #         print("pop:", pd)
    #         print("stack", stackdata)
    #         ret.append(curr.data)
    #         curr=curr.right
    #     return ret
    
    
    def print_tree(self):
        if self.root is None:
            print("empty tree")
        else:
            self._print_tree(self.root,0)
    def _print_tree(self, node, level):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print(' ' * level + str(node.data))
            self._print_tree(node.left, level + 1)

#########test########## 
# bst=bstree()
# bst.insert(4)
# bst.insert(6)
# bst.insert(2)
# bst.insert(1)
# bst.insert(3)
# bst.insert(5)
# bst.insert(7)
# print("===binary search tree===")
# bst.print_tree()

# print("8??:" , bst.search(8))
# print("3??:" , bst.search(3))

# bst.display_inorder()

# ret=bst.inorder_stact()
# print("ret:", ret)

# bst.remove(4)
# bst.print_tree()


# B=[1,4,2,3,1,4,2,3,1,2]
# p1=bstree()
# for i in B:
#     p1.insert(i)
# p1.print_tree()
# ret=p1.inorder_stact()
# print(ret)


##############heap###########
class minheap:
    def __init__(self):
        self.heap=[]
    
    def _parent(self,idx):
        #(idx-1)//2
        return (idx-1)//2
    
    def _left_child(self, idx):
        return (idx*2)+1
    
    def _right_child(self, idx):
        return (idx*2)+2

    ###insert
    def insert_heap(self,data):
        self.heap.append(data)
        self._heapify_up(len(self.heap)-1)
        
    def _heapify_up(self, idx):
        pidx=self._parent(idx)
        while idx>0 and self.heap[idx]<self.heap[pidx]:
            self.heap[idx], self.heap[pidx]=self.heap[pidx],self.heap[idx]
            idx=pidx
            pidx=self._parent(idx)
            
        
    ###delete  
    def extract_min(self):
        if self.heap is None:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return min_val
    
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


# ######test
# th=minheap()
# print(th.heap)
# th.insert_heap(5)
# th.insert_heap(6)
# th.insert_heap(2)
# th.insert_heap(8)
# th.insert_heap(12)
# th.insert_heap(7)
# th.insert_heap(14)
# th.insert_heap(9)
# print(th.heap)

# print(th.extract_min())

# print(th.heap)


##########pqueue
class pqueue:
    def __init__(self):
        self.heap=[]
    def _parent(self, idx):
        return (idx-1)>>1
    def _left_child(self, idx):
        return (idx<<1)+1
    def _right_child(self, idx):
        return (idx<<1)+2
    
    def insert_pq(self, priority, data):
        self.heap.append([priority, data])
        self._heapify_up(len(self.heap)-1)
        
    def _heapify_up(self,idx):
        pidx=self._parent(idx)
        while idx>0 and self.heap[idx][0]<self.heap[pidx][0]:
            self.heap[idx], self.heap[pidx]=self.heap[pidx],self.heap[idx]
            idx=pidx
            pidx=self._parent(idx)
            
    def pq_pop(self):
        if self.heap is None:
            return None
        if len(self.heap)==1:
            return self.heap.pop()[1]
        
        min_val =self.heap[0][1]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return min_val
    
    def _heapify_down(self, idx):
        lenh= len(self.heap)
        while True:
            lidx=self._left_child(idx)
            ridx=self._right_child(idx)
            min_idx=idx
            if lidx<lenh and self.heap[lidx][0]<self.heap[min_idx][0]:
                min_idx=lidx
            if ridx<lenh and self.heap[ridx][0]<self.heap[min_idx][0]:
                min_idx=ridx
            if min_idx==idx:
                break
            
            self.heap[idx],self.heap[min_idx] = self.heap[min_idx],self.heap[idx]
            idx=min_idx


######Test      
# pq=pqueue()
# pq.insert_pq(5,"task 1")
# pq.insert_pq(3,"task 2")
# pq.insert_pq(1,"task 3")
# print(pq.heap)
# print(pq.pq_pop())
# print(pq.heap)


#########hash table
class htable:
    def __init__(self,size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self,key):
        return hash(key)%self.size
    
    def insert(self,key,value):
        idx = self._hash(key)
        for i in self.table[idx]:
            if i[0]==key:
                i[1]=value
                return
        self.table[idx].append([key,value])
    def delete(self,key):
        idx = self._hash(key)
        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                del self.table[idx][i]
                return True #
            return False #
        
# ###test
# test_table = htable()
# test_table.insert("a", 100)
# test_table.insert("b", 200)
# test_table.insert("c", 300)
# test_table.insert("d", 400)
# print(test_table.table)
# test_table.delete("b")
# print(test_table.table)


###linked list

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class htbl:
    def __init__(self, size=10):
        self.size = size
        self.table = [None]*size

    def _hash(self,key):
        return hash(key)%self.size

    def insert(self,key,value):
        idx = self._hash(key)
        nnode = Node(key,value)

        if self.table[idx]==None: #
            self.table[idx] = nnode
            return

        else: #끝에다가
            curr = self.table[idx]
            while curr:
                if curr.key ==key:
                    curr.value = value
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = nnode

    def search(self,key):
        idx = self._hash(key)
        curr = self.table[idx]
        while curr:
            if curr.key ==key:
                return curr.value
            curr = curr.next
        return None

    def delete(self,key):
        idx = self._hash(key)
        curr=self.table[idx]
        prev = None

        while curr:
            if curr.key == key:
                if prev is None: #head
                    self.table[idx] = curr.next
                else:
                    prev.next = curr.next
                return True
            prev =curr
            curr = curr.next

        return False

    def print_table(self):
        for i in range(0, len(self.table)):
            print("idx:",i, end=" ")
            curr = self.table[i]
            while curr:
                print("[key:",curr.key,"val:", curr.value,"]",end=" ")
                curr=curr.next
            print("")


ht = htbl()
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("grape", 300)
ht.print_table()
ht.insert("banana", 250) 
ht.insert("orange", 400)
ht.insert("melon", 100)
ht.insert("cherry", 200)
ht.insert("carrot", 400)
ht.print_table()
ht.delete("banana")
ht.print_table()
ht.delete("apple")