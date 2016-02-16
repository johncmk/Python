'''
Recursive mergeSort
'''

def mergeSort(li):
    if len(li) <= 1:
        return li
    mid = len(li)/2
    left = li[:mid]
    right = li[mid:]
    l = mergeSort(left)
    r = mergeSort(right)
    m = []
    return merge(l,r,m)

def merge(l,r,m):
    if len(l) + len(r) != 0:
        if len(l) == 0:
            m.append(r.pop(0))
        elif len(r) == 0:
            m.append(l.pop(0))
        elif l[0] <= r[0]:
            m.append(l.pop(0))
        elif r[0] <= l[0]:
            m.append(r.pop(0))
        return merge(l,r,m)
    return m 

li = [5,5,4,3,2,1,0,0]

print mergeSort(li)