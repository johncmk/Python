import random

#ver 1
def qsort(li):
    if len(li) <= 1:
        return li
    p_adr = random.randrange(0,len(li))
    p = li[p_adr]
    l,eq,r = [],[],[]
    for i in range(0, len(li)):
        if i == p_adr:
            continue
        else:
            temp = li[i]
            if temp < p:
                l.append(temp)
            elif temp > p:
                r.append(temp)
            else:
                eq.append(temp)
    return qsort(l) + eq + [p] + qsort(r)

#Ver 2
def qsort2(li):
    if len(li) <= 1:
        return li
    pivot = random.choice(li)
    l,eq,r = [],[],[]
    for el in li:
        if el < pivot:
            l.append(el)
        elif el > pivot:
            r.append(el)
        else:
            eq.append(el)
    return qsort2(l) + eq + qsort2(r)

def quickSelect(li,k):
    if li <= 1:
        return li
    p_adr = random.randrange(0, len(li))
    pivot = li[p_adr]
    l,eq,r = [],[],[]
    for i in range(0, len(li)):
        if p_adr == i:
            continue
        else:
            temp = li[i]
            if temp < pivot:
                l.append(temp)
            elif temp > pivot:
                r.append(temp)
            else:
                eq.append(temp)

    if len(l) + len(eq) + 1 == k:
        return pivot
    if len(l) + len(eq) >= k:
        return quickSelect(l+eq, k)
    k = k - ( len(l) + len(eq) + 1)
    return quickSelect(r,k)

#MergeSort
def mergeSort(li):
    if len(li) <= 1:
        return li
    mid = len(li)/2
    l = li[:mid]
    r = li[mid:]
    l = mergeSort(l)
    r = mergeSort(r)
    return merge(l,r)

#merge Ver 1
def merge(l,r):
    if len(l) == 0:
        return r
    if len(r) == 0:
        return l
    if l[0] <= r[0]:
        return [l[0]] + merge(l[1:], r)
    return [r[0]] + merge(l, r[1:])

#MergeSort
def mergeSort2(li):
    if len(li) <= 1:
        return li
    mid = len(li)/2
    l = li[:mid]
    r = li[mid:]
    return merge2(mergeSort(l),mergeSort(r))


#merge Ver2
def merge2(l,r):
    m = []
    lpt = 0
    rpt = 0
    mpt = 0
    llen = len(l)
    rlen = len(r)

    while llen + rlen > len(m):
        if lpt == llen:
            m.append(r[rpt])
            rpt+=1
        elif rpt == rlen:
            m.append(l[lpt])
            lpt+=1
        elif l[lpt] <= r[rpt]:
            m.append(l[lpt])
            lpt+=1
        else:
            m.append(r[rpt])
            rpt+=1
    return m

if __name__ == "__main__":
    li = [5,1,3,2,1,7,7]
    k = 3
    k2 = 1
    k3 = len(li)
    print "QuickSort Version 1 : ",qsort(li)
    print "QuickSort Version 2 : ",qsort2(li)

    print "3rd el : ",quickSelect(li,k)
    print "smallest el : ",quickSelect(li,k2)
    print "biggest el : ",quickSelect(li,k3)

    print "MergeSort Version 1 : ",mergeSort(li)
    print "MergeSort Version 2 : ",mergeSort2(li)


    
