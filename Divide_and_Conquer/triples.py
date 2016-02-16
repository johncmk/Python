'''find triples in array such that a+b=c'''

'''O(n^2)'''
def tripleHash(li,d = {}):
    if len(li) <= 2:
        return li
    for el in li:
        d[-el] = el
    for i, x in enumerate(li):
        for y in li[i+1:]:
            tmp = -(x+y)
            if  tmp in d:
                print x, '+' ,y, '=' ,d[tmp]


li = [4,1,3,2,7,4]
tripleHash(li)