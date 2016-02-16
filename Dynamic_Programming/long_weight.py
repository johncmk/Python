def long_weight(li):
    if len(li) == 0:
        return li
    if li[0] < 0:
        incl = 0
    else:
        incl = li[0]
    excl = 0
    for i in range(1,len(li)):
        temp = incl
        incl = max(incl , excl + li[i])
        excl = temp
    return incl

if __name__ == "__main__":
    li = [-1,5,8]
    li2 = [4,1,1,4,2,1]

    print long_weight(li)
    print long_weight(li2)
