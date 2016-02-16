class Tree:
    __slots__ = "root, left, right".split();
    
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
    
def printTree(t,lev= 0):
    if t is None:
        return None
    print '\t' * lev, t.root 
    return printTree(t.left,lev+1), t.root, printTree(t.right,lev+1)    


'''Find the closet number to given number in BST
Implementation of Binary Search'''

from sys import maxint
        
def find(t,n,parent = None, minVar = maxint):
    if t is None:
        return parent if abs(parent-n) == minVar else minVar + n
    l,root,r = t.left,t.root,t.right
    if n == root:
        return root
    pivot = abs(n - root)
    if pivot < minVar:
        minVar = pivot
    return find(l,n,root,minVar) if n < root else find(r,n,root,minVar)
        
t = Tree(5,Tree(3,Tree(2),Tree(4)),Tree(7,Tree(6),Tree(8)))
print find(t, 6.7)