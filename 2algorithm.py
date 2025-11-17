
#########sort algorithm###########


###selection sort
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

######time check
import random
import time
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
       




#########Seach algorithm###########

##sequential search
def lin_search(L,n):
    for i in range(len(L)):
        if L[i]==n:
            return i
    return -1

##binary search
def bin_search(L,n):
    start=0
    end=len(L)-1
    while start<=end:
        middle=(start+end) >>1
        if L[middle]<n:
            start=middle+1
        elif L[middle]>n:
            end=middle-1
        else:
            return middle
    return -1

##interpolation search
def inter_search(L,n):
    low=0
    high=len(L)-1
    while n>=L[low] and n<=L[high] and low<=high:
        x = (high-low)*(n-L[low])/(L[high]-L[low])+low
        x=int(x)
        
        if L[x]==n:
            return x
        elif L[x]<n:
            low=x+1
        else:
            high=x-1
    return -1
        

######time cheeck

# def rand_list(n):
#     L=[]
#     cnt=0
#     while cnt<n:
#         a=random.randrange(n*100)
#         if a not in L:
#             L.append(a)
#             cnt=cnt+1
#     return L

# def compare_linear_bin():
#     for i in range(10,1000,100):
#         print("data length:", i)
#         Ltime=0
#         Btime=0
#         for j in range(0,2000):
#             L=rand_list(i)
#             L.sort()
#             n=random.randrange(i*100)
#             start=time.time()
#             lin_search(L,n)
#             end=time.time()
#             Ltime=Ltime+(end-start)
            
#             start=time.time()
#             bin_search(L,n)
#             end=time.time()
#             Btime=Btime+(end-start)
#         print(f"Linear search: {Ltime:.5f} sec")
#         print(f"Binary search: {Btime:.5f} sec")


# def compare_linear_bin_unsort():
#     for i in range(10,1000,100):
#         print("data length:", i)
        
#         Ltime=0
#         Btime=0
#         for j in range(0,2000):
#             L=rand_list(i)

#             n=random.randrange(i*100)
#             start=time.time()
#             lin_search(L,n)
#             end=time.time()
#             Ltime=Ltime+(end-start)
            
#             start=time.time()
#             L.sort()
#             bin_search(L,n)
#             end=time.time()
#             Btime=Btime+(end-start)
#         print(f"Linear search: {Ltime:.5f} sec")
#         print(f"Sort+Binary search: {Btime:.5f} sec")


# compare_linear_bin()
# compare_linear_bin_unsort()


##########test###########
L=[4,2,6,5,1,3,0]

print(selection_sort(L))
print(bubble_sort(L))
print(insert_sort(L))

print(merge_sort(L, 0, len(L)-1))


L=[9,8,1,2,7,3,6,4,5]
print(lin_search(L,3))
print(lin_search(L,10))