'''
Shortest Path
@author: John
'''

'''Tree class'''
class Tree:
    __slots__ = "root, left, right".split()
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

    '''If Tree has no child return T else F'''
    def empty(self):
        return True if self.left is None and self.right is None else False

    '''Get root value of the tree'''
    def getRoot(self):
        return self.root

'''Print tree in Pre-order'''        
def printTree(t, tab = 0):
    if t is None:
        return 
    print tab*'\t', t.getRoot()
    printTree(t.left,tab+1)
    printTree(t.right,tab+1)

'''Solution a: using 2 recursions to find the two nodes, and compare their paths to root'''
    
'''Find the LCA(Lowest Common Ancestor) of the BST'''
def findLCA(t,a,b,):
    if t is None:
        return t
    elif t.root > a and t.root > b:
        return findLCA(t.left,a,b)
    elif t.root < a and t.root < b:
        return findLCA(t.right,a,b)
    return shortestPath(t,a,b)

'''ShortestPath using LCA send pointer to left and right side'''
def shortestPath(t,left,right):
    if left > right:
        left,right = right,left
    l,r = 0,0
    if t.root == left and t.root == right:
        return 0
    elif t.root == left:
        return l + findTarget(t.right,right)
    elif t.root == right:
        return findTarget(t.left,left) + r
    return findTarget(t.left,left) + findTarget(t.right,right)

'''locate the node in BST'''    
def findTarget(t,target,length = 1):
    if t.root == target:
        return length
    length+=1
    if t.root > target:
        return findTarget(t.left,target,length)
    return findTarget(t.right,target,length)

'''Solution b: using one recursion'''


    
t = Tree(5,Tree(3,Tree(2)),Tree(7,Tree(6),Tree(8)))

printTree(t)
print "Shortest Path value from 5 to 3 is ",findLCA(t,5,3)




    