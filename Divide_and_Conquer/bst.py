'''BST'''
class Tree():
    __slots__ = "root,left,right".split()

    def __init__(self, root = None , left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

'''preorder'''
def print_t(t, tab=1):
    if t is None:
        return
    l = t.left
    rt = t.root
    r = t.right
    print '\t'*tab,rt
    print_t(l,tab+1)
    print_t(r,tab+1)

'''inorder; to input empty list so you don't get persistance list
    i.e. _sorted(t,[])'''
def _sorted(t,li):
    if t is None:
        return
    l = t.left
    rt = t.root
    r = t.right
    _sorted(l,li)
    li.append(rt)
    _sorted(r,li)
    return li
    
'''Search node logn; if node is found
then return the node else return its parent'''
def _search(t,x,parent = None):
    if t is None:
        return parent
    l = t.left
    rt = t.root
    r = t.right
    if rt == x:
        return t
    elif rt < x:
        return _search(r,x,t)
    return _search(l,x,t)

'''return true if node exists else false'''
def search(t,x):
    sub_t = _search(t,x)
    root = sub_t.root
    if root != x:
        return False
    return True

'''insert'''
def insert(t,x):
    sub_t = _search(t,x)
    root = sub_t.root
    if root == x:
        print x," already exists "
        return
    #else root is the parent of the spot
    if root < x and sub_t.right is None:
        sub_t.right = Tree(x)
    else:
        sub_t.left = Tree(x)


''' ONLY used when delete tree which returns found tree and its parent'''
def _search_parent(t,x,parent = None):
    if t is None:
        return None,None
    l = t.left
    rt = t.root
    r = t.right
    if rt == x and parent is not None:
        return parent,t
    if rt == x and parent == None:
        print x, " is the root node of the tree, thus the parent is itself"
        return None,t
    parent = t
    if rt < x:
        return _search_parent(r,x,parent)
    return _search_parent(l,x,parent)

'''4 cases; 1 no child; remove the entire spot
            2 only left child; override parent's left subtree 
            3 only right child; override parent's right subtree
            4 both child exits; brings the parent'''
def delete(t,x):

    parent,t = _search_parent(t,x)
    
    if t is None and parent is None:
        print x," not exists in BST"
        return

    l = t.left
    rt = t.root
    r = t.right    

    #these can't be done witou parent node
    if l is None and r is None: 
        _delete(parent,rt,None)
    elif l is not None and r is None:
        _delete(parent,rt,l)
    elif l is None and r is not None:
        _delete(parent,rt,r)
    else:
        key = min(_sorted(r,[]))
        delete(t,key)
        t.root = key
        

'''delete support'''
def _delete(parent,rt,sub_t):
    if parent.root < rt:
        parent.right = sub_t
    else:
        parent.left = sub_t

    
if __name__ == "__main__":

    
    t = Tree(4,
                Tree(2,
                     Tree(1),
                     Tree(3)),
                Tree(6,
                     Tree(5),
                     Tree(7,None,
                          Tree(9)
                          )))


    
    print_t(t)
    insert(t,0)
    print_t(t)
    delete(t,9)
    delete(t,0)
    delete(t,6)
    

    insert(t,15)
    print_t(t)
    print _sorted(t,[])
    print "111 exists? ",search(t,111)
    
    insert(t,10)
    insert(t,8)
    insert(t,12)
    insert(t,18)
    print_t(t)
    print _sorted(t,[])
       
    print "15 exists? ",search(t,15)
    print _sorted(t,[])
    
    delete(t,6)
    delete(t,18)
    delete(t,8)
    delete(t,10)
    print_t(t)
    print _sorted(t,[])
    
    insert(t,11)
    print_t(t)
    print "11 exists? ", search(t,11)
    insert(t,10)
    insert(t,0)
    print_t(t)
    print _sorted(t,[])
    delete(t,10)
    delete(t,0)
    delete(t,6)
    print_t(t)
    print _sorted(t,[])
