def lessThan(x,y):
    return x[0]+x[1] < y[0]+y[1] or (x[0]+x[1] == y[0]+y[1] and x[1] < y[1])

'''a) sort solution'''
import random

def qSort(li):
    if len(li) == 0:
        return li
    pAd = random.randint(0,len(li)-1)
    pivot = li[pAd]
    l,eq,r = [],[],[] 
    for x in li:
        if lessThan(x,pivot):
            l.append(x)
        elif lessThan(pivot,x):
            r.append(x)
        else:
            eq.append(x)
    return qSort(l) + eq + qSort(r)

def nbesta(a,b,m = []):
    if len(a) == 0 or len(b) == 0:
        return a+b
    for x in a:
        for y in b:
            m+=[(x,y)]
    return qSort(m)[:len(a)]

'''b) quick select solution'''
def nbestb(a,b,m = []):
    if len(a) == 0 or len(b) == 0:
        return a+b
    for x in a:
        for y in b:
            m+=[(x,y)]
    return qSelect(m,4)

def qSelect(li,k):
    if len(li) == k or len(li) == 0:
        return li
    pAd = random.randint(0,len(li)-1)
    pivot = li[pAd]
    l,eq,r = [],[],[]
    for x in li:
        if lessThan(x,pivot):
            l.append(x)
        elif lessThan(pivot,x):
            r.append(x)
        else:
            eq.append(x)
    if len(l) + len(eq) == k:
        return l+eq
    elif len(l)+len(eq) > k:
        return qSelect(l+eq,k)
    k = k - len(l) - len(eq)
    return l+eq+ qSelect(r,k)

'''c) Dijkstra style best first search only enumerate n or 2n
2nlogn + n == nlogn'''
def nbestc(a,b):
    if len(a) == 0 or len(b) == 0:
        return a+b
    li = sorted(a) #Assume they are sorted in any nlogn sort algorithm
    li2 = sorted(b)
    return _nbestc(li,li2,[0,0],[0,0],[(li[0],li2[0])])

def _nbestc(a,b, aptr, bptr, li = []):
    if len(li) == len(a): # you can use any number of n size of a or b
        return li
    for _ in range(len(a)):
        atmp = (a[aptr[0]],b[aptr[1]+1])
        btmp = (a[bptr[0]+1],b[bptr[0]])
        if lessThan(atmp,btmp):
            li.append(atmp)
            aptr[1]+=1
            return _nbestc(a,b,aptr,bptr,li)
        elif lessThan(btmp,atmp):
            li.append(btmp)
            bptr[0]+=1
            return _nbestc(a,b,aptr,bptr,li)
            
a,b = [4,1,5,3],[2,6,3,4] 

print nbesta(a,b) 
print nbestb(a,b)
print nbestc(a,b)