
#########selection sort###########
def selection_sort(L):
    for i in range(len(L)):
        idx=i
        for j in range(i+1, len(L)):
            if L[j]<L[idx]:
                idx=j
            L[i], L[idx] = L[idx], L[i]
    return L
            
####bubble sort###########
def bubble_sort(L):
    for i in range(0, len(L)-1):
        for j in range(0, len(L)-i-1):
            if L[j]>L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

#########insert sort###########
def insert_sort(L):
    for i in range(1, len(L)):
        curr = L[i]
        j = i-1
        while j>=0 and curr<L[j]:
            L[j+1]= L[j]
            j = j-1
        L[j+1] = curr
    return L

#####merge sort###########
def merge(L, start, mid, end):
    l=(mid-start)+1
    r=(end-mid)
    left=[0]*l
    right=[0]*r
    for i in range(l):
        left[i]=L[start+i]
    for i in range(r):
        right[i]=L[mid+1+i]
    i=0
    j=0
    k=start
    while i<l and j<r:
        if left[i]<=right[j]:
            L[k]=left[i]
            i+=1
        else:
            L[k]=right[j]
            j+=1
        k+=1
    while i<l:
        L[k]=left[i]
        i+=1
        k+=1
    while j<r:
        L[k]=right[j]
        j+=1
        k+=1

def merge_sort(L, start, end):
    if start<end:
        mid = (start+end)//2
        merge_sort(L, start, mid)
        merge_sort(L, mid+1, end)
        merge(L, start, mid, end)
    return L

######quick sort###########

def part_list(L, start, end):
    pivot=L[end]
    i=start-1
    for j in range(start, end):
        if L[j]<=pivot:
            i+=1
            L[i], L[j]=L[j], L[i]
    i=i+1
    L[i], L[end]=L[end], L[i]
    return i       

def quick_sort(L, start, end):
    if end<=start:
        return L
    pivot= part_list(L, start, end)
    quick_sort(L, start, pivot-1)
    quick_sort(L, pivot+1, end)
    return L



##########test###########
L=[4,2,6,5,1,3,0]

print(selection_sort(L))
print(bubble_sort(L))
print(insert_sort(L))

print(merge_sort(L, 0, len(L)-1))

# import random
# import time
# def gen_rand_list(n,a):
#     L=[]
#     for i in range(n):
#         L.append(random.randint(0,a))  
#     return L   

# def copy_list(L):
#     C=[]
#     for i in L:
#         C.append(i)
#     return C

# def test_sort_speed(n):
#     time_isort=0
#     time_ssort=0
#     time_msort=0
#     time_qsort=0
#     for i in range(1000):
#         L1=gen_rand_list(n,n*2)
#         L2=copy_list(L1)
#         L3=copy_list(L1)
#         L4=copy_list(L1)
        
#         start=time.time()
#         insert_sort(L1)
#         end=time.time()
#         time_ssort+=end-start
        
#         start=time.time()
#         selection_sort(L2)
#         end=time.time()
#         time_ssort+=end-start
        
#         start=time.time()
#         quick_sort(L3,0,n-1)
#         end=time.time()
#         time_qsort+=end-start
        
#         start=time.time()
#         merge_sort(L4,0,n-1)
#         end=time.time()
#         time_msort+=end-start
        
#     print("==sort speed test length", n)
#     print(f"selection sort time: {time_ssort:.5f} sec")
#     print(f"insert sort time: {time_isort:.5f} sec")
#     print(f"quick sort time: {time_qsort:.5f} sec")
#     print(f"merge sort time: {time_msort:.5f} sec")
    
# test_sort_speed(10)
# test_sort_speed(1000)       
       
