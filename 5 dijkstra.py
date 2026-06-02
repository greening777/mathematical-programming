
####greedy algorithm - 꼭 최적을 보장하진 않음
def min_coin(N):
    L=[500,100,50,10]
    ret=0
    tmpN=N
    for i in L:
        ret = ret+(tmpN//i)
        tmpN=tmpN%i
    return ret
print(min_coin(1260))


N=int(input())
L=[]
for i in range(N):
    s,e = map(int,input().split())
    L.append([s,e])
    
def max_con(L):
    L.sort(key=lambda x:x[1])
    cnt=0
    end_time=0
    
    for s, e in L:
        if s>=end_time:
            cnt=cnt+1
            end_time=e
    return cnt

print(max_con(L))


L=[[10,60], [20,100], [30,120]]
def bf(L,w):
    ret=[]
    for i in range(0,2**(len(L))):
        tmpw=0
        tmpv=0
        for j in range(0, len(L)):
            tmpw=tmpw+((i>>j)&1)*L[j][0]
            tmpv=tmpv+((i>>j)&1)*L[j][1]
        if tmpw<=w:
            ret.append(tmpv)
    ret.sort()
    return ret[-1]

print(bf(L,50))


L=[[10,60], [20,100], [30,120]]
def real_val(L,w):
    d=[[0]*(w+1) for _ in range(len(L)+1)]
    for i in range(1, len(L)+1):
        cw, cv=L[i-1]
        for j in range(0,w+1):
            if j<cw:
                d[i][j]=d[i-1][j]
            else:
                d[i][j]=max(d[i-1][j],d[i-1][j-cw]+cv)
    return d[len(L)][w]

print(real_val(L,50))



import heapq

L=[[[1,4],[2,2]],[[2,3],[3,2],[4,3]],[[1,1],[3,4],[4,5]],[],[[3,1]]]

def dijk(graph, start):
    dist = [float('inf') for _ in range(len(graph))]
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

ret=dijk(L,0)
print(ret)


n,m=map(int,input().split())
L=[[] for _ in range(n+1)]

for _ in range(m):
    s,e,d=map(int, input().split())
    L[s].append([e,d])

x,y=map(int,input().split())

def is_distance(L,x,y):
    d=[float('inf') for _ in range(len(L))]
    d[x]=0
    pq=[(0,x)]
    
    while pq:
        cd,cn=heapq.heappop(pq)
        
        if cd>d[cn]:
            continue
        
        for v,w in L[cn]:
            if d[v]>d[cn]+w:
                d[v]=d[cn]+w
                heapq.heappush(pq, (d[v],v))
    return d[y]

print(is_distance(L,x,y))