'''
Recursive mergeSort
'''
#!/user/bin

def mergesort(li):
    if len(li) <= 1:
        return li
    mid = len(li)/2
    l = li[:mid]
    r = li[mid:]
    l = mergesort(l)
    r = mergesort(r)
    return merge(l,r)

'''LinkedList Style merge'''
# def merge(l,r):
#     if l == []:
#         return r
#     if r == []:
#         return l
#     if l[0] >= r[0]:
#         return [r[0]] + merge(l,r[1:])
#     return [l[0]] + merge(l[1:],r)

''' merge ver 1 '''
def merge(l,r):
    m = []
    total_len = len(l) + len(r)
    l_ptr, r_ptr = 0,0
    while total_len > (l_ptr + r_ptr):
        if l_ptr == len(l):
            m.append(r[r_ptr])
            r_ptr+=1
        elif r_ptr == len(r):
            m.append(l[l_ptr])
            l_ptr+=1
        elif l[l_ptr] < r[r_ptr]:
            m.append(l[l_ptr])
            l_ptr+=1
        else:
            m.append(r[r_ptr])
            r_ptr+=1
    return m

''' merge ver 2 '''
# def merge(l,r,m = []):
#     if len(l) + len(r) != 0:
#         if len(l) == 0:
#             m.append(r.pop(0))
#         elif len(r) == 0:
#             m.append(l.pop(0))
#         elif l[0] <= r[0]:
#             m.append(l.pop(0))
#         elif r[0] <= l[0]:
#             m.append(r.pop(0))
#         return merge(l,r,m)
#     return m 


if __name__ == "__main__":
    li = [5,1,2,3,2,0,2,11]
    print mergesort(li)
