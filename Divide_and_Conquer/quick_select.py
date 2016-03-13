'''
Quick Select
Best O(n)
Worst O(n^2)
@author: John
'''
import random

def qselect(li, k):    
    if li == []:
        return li
    p_adr = random.randrange(len(li))
    pivot = li[p_adr]
    l,eq,r = [],[],[]
    for i in range(len(li)):
        if i == p_adr:
            continue
        else:
            temp = li[i]
            if temp < pivot:
                l.append(temp)
            elif temp > pivot:
                r.append(temp)
            else:
                eq.append(temp)
     
    if len(l)+len(eq)+1 == k:
        return pivot
    if len(l)+len(eq) >= k:
        return qselect(l+eq, k)
    k = k - (len(l) + len(eq) + 1)
    return qselect(r, k)

if __name__ == "__main__":
    
    li = [3,10,4,7,19]
    li2 = [11,2,8,3]
    print qselect(li, len(li))
    print qselect(li2, 4)