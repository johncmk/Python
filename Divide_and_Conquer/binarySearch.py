'''Binary Search Time complexity O(logN)'''

def bsearch(k,li):
    if len(li) == 2 and (li[0] and li[1] != k):
        return li,"k not in the list"
    m = int(len(li)/2)
    if li[m] == k:
        return k
    if k < li[m]:
        return bsearch(k,li[:m])
    if k > li[m]:
        return bsearch(k,li[m:])
        
li = [-1, 5, 6, 18, 19, 25, 46, 78, 102, 114]
k = 103

print(bsearch(k,li))

