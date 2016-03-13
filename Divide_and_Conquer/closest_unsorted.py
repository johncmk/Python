import random

def closest_unsorted(li,x, k):
    if li == [] or len(li) == k:
        return li
    p_adr = random.randrange(0,len(li))
    pivot = abs(x-li[p_adr])
    l,eq,r = [],[],[]
    
    for i in range(len(li)):
        if i == p_adr:
            continue
        else:
            temp = abs(x-li[i])
            if temp < pivot:
                l.append(li[i])
            elif temp > pivot:
                r.append(li[i])
            else:
                eq.append(li[i])
    pivot = li[p_adr]
    
    if len(l) + len(eq) + 1 == k:
        return l+eq+[pivot]
    if len(l) + len(eq) >= k:
        return closest_unsorted(l+eq,x,k)
    k = k- (len(l) + len(eq) + 1)
    return l+eq+closest_unsorted(r,x,k)

if __name__ == "__main__":
    x = 5.2
    k = 2
    li = [4,1,3,2,7,4]
    print closest_unsorted(li, x, k)
    
    x = 6.5
    k = 3
    print closest_unsorted(li, x, k)