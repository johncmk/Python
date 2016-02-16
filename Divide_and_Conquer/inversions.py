inversion = 0

def foo(li):
    if len(li) <= 1:
        return li
    mid = len(li)/2
    l,r = [],[]
    for i,el in enumerate(li):
        l.append(el) if(i < mid) else r.append(el)
    left = foo(l)
    right = foo(r)
    global inversion
    print inversion
    return merge(left,right)

def merge(l,r):
    print 'l ',l 
    print 'r ',r 
    if l == []:
        return r
    if r == []:
        return l
    global inversion
    inversion += len(l)
    if l[0] < r[0]:
        return [l[0]] + merge(l[1:],r)
    else:
        return [r[0]] + merge(l,r[1:])

li= [3,1,4,2]
print foo(li)
print 'inv ', inversion