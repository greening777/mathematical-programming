##########generate random vector##########
import random

def gen_vec(n,a):
    #n=dimension, a=range
    ret = []
    for _ in range(n):
        ret.append(random.randrange(-a,a))
    return ret

def gen_vec2(n,a):
    ret=[0]*n
    for i in range(n):
        ret[i]=random.randrange(-a,a)
    return ret

def gen_zero_vec(n):
    #zero vector of dimension n
    ret= [0]*n
    return ret

v=gen_vec(3,5)
print("v dimension:", len(v))
print(gen_zero_vec(5))


##########matrix calcula tion##########

def gen_zero_mat(m,n):
    #zero matrix of dimension n*m
    ret = []
    for _ in range(m):
        v=gen_zero_vec(n)
        ret.append(v)
    return ret

A=gen_zero_mat(3,2)
print(A)
print("A row", len(A))
print("A col", len(A[0]))


def gen_identity_mat(n):
    I=gen_zero_mat(n,n)
    for i in range(n):
        I[i][i]=1
    return I

print(gen_identity_mat(3))

def is_same_mat(A,B):
    rowA=len(A)
    colA=len(A[0])
    rowB=len(B)
    colB=len(B[0])
    if rowA!=rowB:
        return False
    if colA!=colB:
        return False
    for i in range(rowA):
        for j in range(colA):
            if A[i][j]!=B[i][j]:
                return False 
    return True

A=[[1,2],[3,4],[5,6]]
B=[[1,2],[3,4]]
C=[[1,2],[3,4],[5,5]]
D=[[1,2],[3,4],[5,6]]
print(is_same_mat(A,B))
print(is_same_mat(A,C))
print(is_same_mat(A,D))


def mat_add(A,B):
    rowA=len(A)
    colA=len(A[0])
    rowB=len(B) 
    colB=len(B[0])
    if rowA!=rowB or colA!=colB:
        print("error: dimension mismatch")
        return None
    C=gen_zero_mat(rowA,colA)
    for i in range(rowA):
        for j in range(colA):
            C[i][j]=A[i][j]+B[i][j]
    return C

print(mat_add(A,D))
print(mat_add(A,B))


def mat_mul(A,B):
    rowA=len(A)
    colA=len(A[0])
    rowB=len(B)
    colB=len(B[0])
    if colA!=rowB:
        print("error: dimension mismatch")
        return None
    C=gen_zero_mat(rowA,colB)
    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                C[i][j]+=A[i][k]*B[k][j]
    return C

A=[[1,2]]
B=[[2,3]]
C=[[1,0,1],[2,1,0]]
print(mat_mul(A,B))
print(mat_mul(A,C))



###########determinant##########
def det_22(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def gen_Mij(A,j):
    ret = gen_zero_mat(len(A)-1,len(A)-1)
    for i in range(1,len(A)):
        for k in range(0, len(A)):
            if k<j:
                ret[i-1][k]=A[i][k]
            elif k>j:
                ret[i-1][k-1]=A[i][k]
    return ret
            
def det_nn(A):
    rowA = len(A)
    colA = len(A[0])
    if rowA!=colA:
        print("error: not square matrix")
        return None
    if rowA==2:
        return det_22(A)
    else:
        ret=0 #accumulate det value
        for i in range(colA):
           sign=(-1)**i
           Asub = gen_Mij(A,i)
           ret = ret + sign * A[0][i] * det_nn(Asub)
        return ret
    
A=[[1,2,3],[0,1,4],[5,6,0]]
print(det_nn(A))



#############gussian elimination##########
def copy_mat(A):
    rowA=len(A)
    colA=len(A[0])
    Acpy=gen_zero_mat(rowA,colA)
    for i in range(rowA):
        for j in range(colA):
            Acpy[i][j]=A[i][j]
    return Acpy

def swap_row(A,i,j): #switch row i and row j for pivoting
    A[i],A[j]=A[j],A[i]
    return A


def gaussian_elim(A):
    rowA=len(A)
    colA=len(A[0])
    Acpy=copy_mat(A)
    
    pr=0 #pivot row
    pc=0 #pivot col
    while pr<rowA and pc<colA:
        i = pr
        while Acpy[i][pc]==0 and i+1<rowA:
            i+=1
            
        if Acpy[i][pc]==0 and i+1==rowA:#this column is all zero
            pc+=1
            
        else: #this column has non-zero entry
            swap_row(Acpy,i, pr)
            k= Acpy[pr][pc]
            
            for j in range(colA):
                Acpy[pr][j]=Acpy[pr][j]/k #make pivot=1
            
            for j in range(pr+1,rowA):#eliminate below pivot
                k=Acpy[j][pc]
                for m in range(pc,colA):
                    Acpy[j][m]=Acpy[j][m]-k*Acpy[pr][m]
            pr+=1
            pc+=1
    return Acpy
            
            
A=[[0,2,1,4],[1,1,1,3],[2,1,-1,1]]
print(gaussian_elim(A))    