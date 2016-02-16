'''
Quick Sort
@author: John
'''

import random

def qSort(li):
    if li == []:
        return []
    pAdrs = random.randint(0,len(li)-1)
    pivot = li.pop(pAdrs)
    l = [x for x in li if x <= pivot]
    r = [y for y in li if y > pivot]
    return qSort(l) + [pivot] + qSort(r)

li = [3,4,5,2,10,1,0,2]
print qSort(li)