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


##########matrix calculation##########

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
