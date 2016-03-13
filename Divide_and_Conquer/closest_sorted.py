
def find(li, x ,k):
    if li == [] or len(li) == k:
        return li
    mid = len(li)/2
    pivot = abs(x-li[mid])
    l,eq,r = [],[],[]
    for i in range(len(li)):
        if i == mid:
            continue
        else:
            temp = abs(x-li[i])
            if temp < pivot:
                l.append(li[i])
            elif temp > pivot:
                r.append(li[i])
            else:
                eq.append(li[i])
                
    pivot = li[mid]
    if len(l) + len(eq) + 1 == k:
        return l+eq+[pivot]
    if len(l) + len(eq) >= k:
        return find(l+eq,x,k)
    k = k - (len(l) + len(eq) + 1)
    return l+eq+[pivot]+find(r,x,k)

if __name__ == "__main__":
    li = [1,2,3,4,4,7]
    x = 5.2
    k = 2
    print find(li,x,k)
    x = 6.5
    k = 3
    print find(li,x,k)