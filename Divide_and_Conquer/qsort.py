'''Buggy Quick Sort which creates BST'''
def sort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]

'''Find node in BST return its current position'''
def _search(t,x):
    if t == []:
        return t
    l,root,r = t
    if x == root:
        return t
    if x < root:
        return _search(l,x)
    if x > root:
        return _search(r,x)

'''T if x is in BST else F'''
def search(t,x):
    return False if _search(t,x) == [] else True

'''Insert element into BST'''
def insert(t,x):
    node = _search(t,x)
    if node == []:
        node += [[],x,[]]

'''Infix Traversal is inorder Traversal that is left,root,right'''
def sorted(t):  # @ReservedAssignment
    if t == []:
        return []
    l,root,r = t
    return sorted(l) + [root] + sorted(r)

'''helper function for delete BST'''    
def smallestRight(t):
    l = t[0] 
    return t if l == [] else smallestRight(l)   
    
'''delete node in BST'''    
def delete(t,x):
    node = _search(t,x)
    if node == []:
        return
    l,r = node[0],node[2]
    if l == [] and r == []:
        del node[:]
    elif r != [] and l == []:
        node = r
    elif l != [] and r == []:
        node = l 
    else:
        key = smallestRight(r)
        node[1] = key[1]
        del key[:]

'''Print Tree form'''
def printTree(t,tab = 1):
    if t == []:
        return
    l,root,r = t
    print '\t' *tab,root
    printTree(l,tab+1)
    printTree(r,tab+1)

# li = [4,2,6,3,5,7,1,9]
# liT = sort(li)
# printTree(liT)

# print liT
# print _search(liT, 3)
# print search(liT,6)
# insert(liT,6.5)
# print liT
# print sorted(liT)
# delete(liT,4)
# print liT

# t = sort([2])
# print t
# insert(t,1)
# insert(t,3)
# insert(t,4)
# print t

# printTree([[[],1,[[[],3,[]],4,[]]],5,[[],6,[]]])

printTree([[[],1,[[[],3,[]],4,[]]],5,[[],6,[]]])