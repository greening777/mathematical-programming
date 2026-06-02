import random

def karatsuba_mul(a,b):
    ah=a>>512
    al=a^(ah<<512)
    bh=b>>512
    bl=b^(bh<<512)
    
    albl=al*bl
    ahbh=ah*bh
    mid=(ah+al)*(bh+bl)-albl-ahbh
    ahbh=ahbh<<1024
    mid=mid<<512
    return (albl+ahbh+mid)

a=random.randrange(1,2**1024)
b=random.randrange(1,2**1024)

c=karatsuba_mul(a,b)
d=a*b

print("c==d?", c-d)

def schoolbook_poly(f,g):
    h=[0]*(len(f)<<1)
    for i in range(len(f)):
        for j in range(len(g)):
            h[i+j]+=f[i]*g[j]
    return h

def karatsuba_poly(f,g):
    hlen=len(f)>>1
    fh=f[hlen:]
    fl=f[:hlen]
    gh=g[hlen:]
    gl=g[0:hlen]

    flgl=schoolbook_poly(fl,gl)
    fhgh=schoolbook_poly(fh,gh)
    
    fhl=[0]*hlen
    for i in range(hlen):
        fhl[i]=fh[i]+fl[i]
    ghl=[0]*hlen
    for i in range(hlen):
        ghl[i]=gh[i]+gl[i]
        
    mid=schoolbook_poly(fhl,ghl)
        
    for i in range(len(f)):
        mid[i]=mid[i]-flgl[i]-fhgh[i]
        
    h=[0]*(len(f)<<1)
    for i in range(len(flgl)):
        h[i]=h[i]+flgl[i]
        
    for i in range(len(f), len(f)+len(fhgh)):
        h[i]=h[i]+fhgh[i-len(f)]
    
    for i in range(hlen,hlen+len(mid)):
        h[i]=h[i]+mid[i-hlen]
        
    return h
        
        

f=[4,-2,1,3]
g=[6,1,2,3]

def rand_poly(n):
    f=[]
    for i in range(n):
        f.append(random.randrange(0,10))
    return f


f=rand_poly(10)
print(f)
g=rand_poly(10)
print(g)

h=schoolbook_poly(f,g)
print(h)
g=karatsuba_poly(f,g)
print(g)


import time
time_school=0
time_kara=0
for i in range(100):
    f=rand_poly(100)
    g=rand_poly(100)
    
    start=time.time()
    h=schoolbook_poly(f,g)
    end=time.time()
    time_school=time_school+(end-start)
    
    start=time.time()
    k=karatsuba_poly(f,g)
    end=time.time()
    time_kara=time_kara+(end-start)
    
print(f"schoolbook: {time_school:.5f} sec")
print(f"karatsuba: {time_kara:.5f} sec")