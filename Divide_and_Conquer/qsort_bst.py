'''Buggy Quick Sort which generates BST'''
def quicksort(li):
    if li == []:
        return []
    pivot = li[0]
    left = [el for el in li if el < pivot]
    right = [el for el in li[1:] if el >= pivot]
    return [quicksort(left)] + [pivot] + [quicksort(right)]
 
'''sorted; inorder'''
def _sorted(t):
    if t == []:
        return []
    l,root,r = t
    return _sorted(l) + [root] + _sorted(r)
 
def printTree(t, tab=1):
    if t == []:
        return 
    l, root, r = t;
    print '\t' *tab, root
    printTree(l, tab+1)
    printTree(r, tab+1)
 
'''Search'''
def _search(t,x):
    if t == []:
        return t
    l,root,r = t
    if root == x:
        return t
    if root < x:
        return _search(r,x)
    return _search(l,x)
    
'''search'''
def search(t, x): 
    return False if _search(t, x) == [] else True

'''Insert'''
def insert(t, x):
    res = _search(t,x)
    if res == []:
        res += [[],x,[]]
 
def smallestRight(t):
    l = t[0]
    if l == []:
        return t[1]
    return smallestRight(l)
    
def delete(t,x):
    sub_t = _search(t, x)
    if sub_t == []:
        return []
    l,r = sub_t[0], sub_t[2] 
    if l == [] and r == []:
        del sub_t[:]
    elif l != [] and r == []:
        del sub_t[:]
        sub_t += l
    elif r != [] and l == []:
        del sub_t[:]
        sub_t += r
    else:
        key = smallestRight(r)
        sub_t[1] = key
        delete(r,key)
        
        
if __name__ == "__main__":
    
    li = [4,2,6,3,5,7,1,9]
    t = quicksort(li)
    print t
    print _sorted(t)
    printTree(t)
    delete(t,4)
    printTree(t)
#    printTree([[[],1,[[[],3,[]],4,[]]],5,[[],6,[]]])
#     print _sorted(t)