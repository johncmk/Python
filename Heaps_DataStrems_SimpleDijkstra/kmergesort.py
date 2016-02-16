from math import ceil
from heapq import heappop, heappush,heapify
from copy import deepcopy
from sys import maxint

'''3 way mergesort
O(NlogN based of 3)'''

def kwayMergeSort(li, heap = []):
    cache = {0:[], 1:[], 2:[]}
    var = maxint # dummy value
    if len(li) == 1:
        return li
    mid = int(ceil(len(li)/3.0))
    l = li[:mid]
    md = li[mid:mid*2]
    r =  li[mid*2:]
    total = [l]+[md]+[r]
    for i in range(3):
        heapify(total[i])
        cache[i] = deepcopy(total[i])
        heappush(heap,heappop(total[i]))
    return merge(total,heap,cache,var)

def merge(total, heap, cache ,var, m = []):
    f,s,t = total[0],total[1],total[2] 
    while len(f) + len(s) + len(t) != 0:
        if len(f) > 0 and var in cache[0]:
            heappush(heap, heappop(f))
        if len(s) > 0 and var in cache[1]:
            heappush(heap, heappop(s))
        if len(t) > 0 and var in cache[2]:
            heappush(heap, heappop(t))
        heapify(heap)
        var = heappop(heap)
        m.append(var)
        return merge(total, heap, cache, var, m)
    if len(heap) < 3:
        while heap:
            m.append(heappop(heap))
        return m

li = [4,1,5,2,6,3,7,0]
print kwayMergeSort(li)