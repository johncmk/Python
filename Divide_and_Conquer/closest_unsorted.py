import random

def find(li,x,k):
    if len(li) == k or len(li) <= 0:
        return li
    pAdr = random.randint(0,len(li)-1)
    pivot = li[pAdr]
    pivotFixed = abs(pivot-x)
    l,r,eq = [],[],[]
    for el in li:
        tmp = abs(el-x)
        if tmp < pivotFixed:
            l.append(el)
        elif tmp > pivotFixed:
            r.append(el)
        else:
            eq.append(el)
    if len(l)+len(eq)+1 == k:
        return l + eq + [pivot]
    if len(l)+len(eq) >= k:
        return find(l+eq,x,k)
    k = k - len(l) - 1
    return l+eq+find(r,x,k)

li = [4,1,3,2,7,4]

print find(li,5.2,2)
print find(li,6.5,3)