'''find the closes k amount of number in sorted array list '''


def foo(li,x,k):
    if len(li) == k or len(li) <= 0:
        return li
    mid = len(li)/2
    pivot = li[mid]
    pTmp = abs(pivot-x)
    l,r,eq = [],[],[]
    for el in li:
        tmp = abs(el-x)
        if tmp < pTmp:
            l.append(el)
        elif tmp > pTmp:
            r.append(el)
        else:
            eq.append(el)
    if len(eq) == k:
        return eq
    elif len(l) + len(eq) == k:
        return l+eq
    elif len(l) + len(eq) > k:
        return foo(l+eq,x,k)
    k = k - len(l)-len(eq)
    return l+eq+foo(r,x,k)


li = [4,1,3,2,7,4]

print foo(li,5.2,2)
print foo(li,6.5,3)