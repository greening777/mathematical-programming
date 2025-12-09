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
slist=stack_array()
slist.push(1)
slist.push(2)
slist.push(3)
# print(slist.stack)
# print(slist.pop())
# print(slist.stack)
# print(slist.peek())

slist.print_stack()


lq=queue_list()
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(3)
print(lq.queue)
print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())
print(lq.queue)
print(lq.dequeue())