'''
Quick Sort
@author: John
'''

import random

def qsort(li):
    if li == []:
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
    return qsort(l) + eq + qsort(r)

if __name__ == "__main__":
    li = [5,1,2,4,3,3,5,1,2,4,3]
    print qsort(li)
