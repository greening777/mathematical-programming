# 선택정렬
def select_sort(A):
    for i in range(len(A)):
        idx=i
        for j in range(i+1, len(A)):
            if A[idx]>A[j]:
                idx=j
                A[i], A[idx] = A[idx], A[i]
    return A
                

#버블정렬
def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A


#삽입정렬
def insert_sort(A):
    for i in range(1, len(A)):
        curr = A[i]
        j=i-1
        while j>=0 and curr<A[j]:
            A[j+1] = A[j]
            j=j-1
        A[j+1]=curr
    return A


#합병 정렬
def merge(left, right):
    L=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            L.append(right[j])
            j=j+1
        elif left[i]<=right[j]:
            L.append(left[i])
            i=i+1
    L.extend(left[i:])
    L.extend(right[j:])
    return L

def merge_sort(A):
    if len(A)==1:
        return A
    mid=len(A)//2
    left=merge_sort(A[:mid])
    right=merge_sort(A[mid:])
    return merge(left, right)

        
#quicksort
def quick_sort(A):
    l=[]
    r=[]
    if len(A)<=1:
        return A
    pivot= A[0]
    for i in range(1, len(A)):  
        if A[i]<pivot:
            l.append(A[i])
        elif A[i]>=pivot:
            r.append(A[i])
    l_sort=quick_sort(l)
    r_sort=quick_sort(r)
    return (l_sort + [pivot] + r_sort)
            



L=[4,2,6,5,1,3,0]
print(merge_sort(L))