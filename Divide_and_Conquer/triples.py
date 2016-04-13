
'''Best case and Worst case O(NlogN) used for non-hash triples algorithm'''
def msort(li):
    if len(li) == 1:
        return li
    mid = len(li)/2
    l = li[:mid]
    r = li[mid:]
    l = msort(l)
    r = msort(r)
    return merge(l,r)

def merge(l,r):
    len_l = len(l)
    len_r = len(r)
    l_pt = 0
    r_pt = 0
    m = []

    while len(m) < (len_l + len_r):
        if l_pt == len_l:
            m.append(r[r_pt])
            r_pt+=1
        elif r_pt == len_r:
            m.append(l[l_pt])
            l_pt+=1
        elif l[l_pt] <= r[r_pt]:
            m.append(l[l_pt])
            l_pt+=1
        else:
            m.append(r[r_pt])
            r_pt+=1
    return m


'''Given an array A[] and a number x, check for pair in A[] with sum as x'''

'''Mergesort O(NlogN) + Linear Search O(N) = Thus it's O(NlogN)'''
def hasTwo(li, x):
    if len(li) == 0:
        return
    li = msort(li)
    lm = 0
    rm = len(li)-1

    while lm < rm:
        if li[lm] + li[rm] == x:
            return [li[lm] , li[rm]]
        elif li[lm] + li[rm] < x:
            lm+=1
        else:
            rm-=1
    return ["no two sum number exists in the list"]

'''Time complexity O(n) + O(n) = O(n)'''
def hasTwo_map(li,x):
    if len(li) <= 1:
        return
    d = {}
    for el in li:
        d[el] = 0
    for i in range(len(li)):
        temp = x-li[i]
        if temp in d and li[i] in d and d[temp] == 0:
            return [li[i], temp]
        d[li[i]] = 1
    
'''Given an array of n numbers, find *all* triples (x,y,x) s.t. x+y=z'''

'''a) Solution; using hash table O(n^2)'''
def triples(li):
    if len(li) <= 3:
        return
    d = {}
    for el in li:
        d[el] = 0
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            x = li[i]
            y = li[j]
            temp = x+y
            if temp in d and d[temp] == 0:
                print (x,y,temp)
                d[temp] = 1
            
'''b) Solution; witout using hash table O(nlogn) + O(n) + O(n^2) = O(n^2)
    q is used to prevent duplcations of triples'''

import sys

def triples_li(li):
    if len(li) <= 3:
        return
    li = msort(li) #mergesort
    q = [-sys.maxint] #dummy negative infinite
    
    for i in range(len(li)-1,-1,-1):
        lm = 0 #leftmost
        rm = i #rightmost
        z = li[i]
        while lm < rm:
            x = li[lm]
            y = li[rm]
            if x + y == z:
                el = q[0] #FIFO
                if el != z:
                    print (x,y,z)
                    q.insert(0,z)
                break
            elif x + y < z:
                lm+=1
            else:
                rm-=1
            

'''O(n^2) used mathematic equatoin which is x+y+z = 0 thus z = -(x+y)'''
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

        
if __name__ == "__main__":

    li = [1,4,45,6,10,-8]
    x = 16

    li2 = [4,1,3,2,7,4]
    
    print "x is given; it's easier to find triples"
    print hasTwo(li,x)
    print hasTwo_map(li,x)
    print "x is not given"
    triples(li2)
    triples_li(li2)

