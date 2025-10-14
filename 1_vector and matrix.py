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

##########matrix calcula tion##########

def gen_zero_mat(m,n):
    #zero matrix of dimension n*m
    ret = []
    for _ in range(m):
        v=gen_zero_vec(n)
        ret.append(v)
    return ret

def gen_identity_mat(n):
    I=gen_zero_mat(n,n)
    for i in range(n):
        I[i][i]=1
    return I

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
            


###########inverse matrix##########


def gj_elim(A):
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
            
            for j in range(rowA):#eliminate all other rows
                if j!=pr:
                    k=Acpy[j][pc]
                    for m in range(pc,colA):
                        Acpy[j][m]=Acpy[j][m]-k*Acpy[pr][m]
            pr+=1
            pc+=1
    return Acpy


def ext_mat(A):  ##### [A|I]#####
    rowA=len(A)
    ret=gen_zero_mat(rowA,rowA*2)
    for i in range(rowA):
        for j in range(rowA):
            ret[i][j]=A[i][j]
        ret[i][i+rowA]=1
    return ret


def inv_mat(A):
    rowA=len(A)
    colA=len(A[0])
    if rowA!=colA:
        return None
    Acpy=ext_mat(A) #[A|I]
    
    pr=0
    pc=0
    while pr<rowA and pc<colA:
        i = pr
        while Acpy[i][pc]==0 and i+1<rowA:
            i+=1
            
        if Acpy[i][pc]==0 and i+1==rowA:#this column is all zero
            pc+=1
            
        else: #this column has non-zero entry
            swap_row(Acpy,i, pr)
            k= Acpy[pr][pc]
            
            for j in range(colA*2):
                Acpy[pr][j]=Acpy[pr][j]/k #make pivot=1
            
            for j in range(rowA):#eliminate all other rows
                if j!=pr:
                    k=Acpy[j][pc]
                    for m in range(colA*2):
                        Acpy[j][m]=Acpy[j][m]-k*Acpy[pr][m]
            pr+=1
            pc+=1
    Ainv=gen_zero_mat(rowA,colA)
    for i in range(rowA):
        for j in range(colA):
            Ainv[i][j]=Acpy[i][j+colA]
    return Ainv

###########eigenvalue and eigenvector##########
def is_eigen_val(A,lam):
    rowA=len(A)
    B=copy_mat(A)
    for i in range(rowA):
        B[i][i]=B[i][i]-lam
    #B=A-bI
    if det_nn(B)==0:
        return True
    else:
        return False
    
def is_eigen_vec(A,x):
    Ax=mat_mul(A,x)
    rowA=len(A)
    k=Ax[0][0]/x[0][0]   
    for i in range(rowA):
        if x[i][0]*k != Ax[i][0]:
            return False
    return True 

def eigval_22(A):
    a=A[0][0]
    b=A[0][1]
    c=A[1][0]
    d=A[1][1]
    
    D=(a+d)**2-4*(a*d-b*c)
    D=D**0.5
    lam1=(a+d+D)/2
    lam2=(a+d-D)/2
    return (lam1,lam2)
    
def eigvec_22(A):
    k1, k2 = eigval_22(A)
    x1=[[A[0][1]], [k1 - A[0][0]]]
    x2=[[A[0][1]], [k2 - A[0][0]]]
    return k1,k2, x1,x2
    
########power iteration method##########
def copy_vec(x): #열벡터 복사
    n=len(x)
    ret=[[0] for _ in range(n)]
    for i in range(n):
        ret[i][0]=x[i][0]
    return ret

def diff_vec(v,w):
    n=len(v)
    u=[[0] for _ in range(n)]
    for i in range(n):
        u[i][0]=v[i][0]-w[i][0]
    ret=0
    for i in range(n):
        ret+=u[i][0]**2
    ret=ret**0.5
    return ret
    
def rowvec_to_colvec(rv):
    n=len(rv)
    cv=[[0] for _ in range(n)]
    for i in range(n):
        cv[i][0]=rv[i]
    return cv

def colvec_to_rowvec(cv):
    n=len(cv)
    rv=[0]*n
    for i in range(n):
        rv[i]=cv[i][0]
    return rv

def unit_colvec(cv):
    n=len(cv)
    uv=[[0] for _ in range(n)]
    ret=0
    for i in range(n):
        ret=ret+cv[i][0]**2
    ret=ret**0.5
    for i in range(n):
        uv[i][0]=cv[i][0]/ret
    return uv
        
def colvec_dot(u,v):
    n=len(u)
    ret=0
    for i in range(n):
        ret=ret+u[i][0]*v[i][0]
    return ret

def pim(A,iter, diff, max_cnt):
    flag=0
    cnt=0
    n=len(A)
    while flag==0:
        v=gen_vec(n,10)
        v=rowvec_to_colvec(v)
        v=unit_colvec(v)
        t=copy_vec(v)
        
        for i in range(iter):
            v=mat_mul(A,v)
            v=unit_colvec(v)
            delta=diff_vec(v,t)
            t=copy_vec(v)
        cnt+=1
        
        if delta<diff:
            flag=1
        if cnt>max_cnt:
            return 
    #find
    Av=mat_mul(A,v)
    Av_v=colvec_dot(Av,v)
    v_v=colvec_dot(v,v)
    k=Av_v/v_v
    return v, k










    
#####################################test##############3#########
v=gen_vec(3,5)
print("v dimension:", len(v))
print(gen_zero_vec(5))


A=gen_zero_mat(3,2)
print(A)
print("A row", len(A))
print("A col", len(A[0]))


print(gen_identity_mat(3))


A=[[1,2],[3,4],[5,6]]
B=[[1,2],[3,4]]
C=[[1,2],[3,4],[5,5]]
D=[[1,2],[3,4],[5,6]]
print(is_same_mat(A,B))
print(is_same_mat(A,C))
print(is_same_mat(A,D))

print(mat_add(A,D))
print(mat_add(A,B))

A=[[1,2]]
B=[[2,3]]
C=[[1,0,1],[2,1,0]]
print(mat_mul(A,B))
print(mat_mul(A,C))


A=[[1,2,3],[0,1,4],[5,6,0]]
print(det_nn(A))


A=[[0,2,1,4],[1,1,1,3],[2,1,-1,1]]
print(gaussian_elim(A))

A=[[1,2,3],[0,1,4],[5,6,0]]

    #eigenvalue check
A=[[6,-1],[2,3]]
print("is 5 eigenvalue?", is_eigen_val(A,5))
print("is 5 eigenvalue?", is_eigen_val(A,4))
print("is 5 eigenvalue?", is_eigen_val(A,3))
print("is 5 eigenvalue?", is_eigen_val(A,2))

x1=[[1],[-1]]
x2=[[1],[1]]
x3=[[1],[2]]

print("is x1 eigenvector?", is_eigen_vec(A,x1))
print("is x2 eigenvector?", is_eigen_vec(A,x2))
print("is x3 eigenvector?", is_eigen_vec(A,x3))

print("eigenvalues", eigval_22(A))

k1,k2,x1,x2=eigvec_22(A)
print("eigenvalue1:", k1, "eigenvector1:", x1)
print("eigenvalue2:", k2, "eigenvector2:", x2)

v,k =pim(A,100, 0.001, 10)
print("eigenvalue:", k,  "\neigenvector:", v)