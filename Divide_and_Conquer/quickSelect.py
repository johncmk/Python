'''
Quick Select
Best O(n)
Worst O(n^2)
@author: John
'''

import random

def foo(k, li):
    if len(li) <= 1:
        return li[0]
    pAdr = random.randint(0,len(li)-1)
    pivot = li.pop(pAdr)
    l = [x for x in li if x <= pivot]
    r = [x for x in li if x > pivot]
    if len(l) + 1 == k:
        return pivot
    if len(l) >= k:
        return foo(k,l)
    k = k - (len(l) + 1 )
    return foo(k,r)

li = [3,10,4,7,19]
li2 = [11,2,8,3]

print foo(2,li)
print foo(4,li2)