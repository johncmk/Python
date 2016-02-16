import heapq
m = [] # median numbers

'''
Find median number in data stream
O(n) linear algorithm'''
def medians(li, minH = [], maxH = []):
    if len(li) <= 1:
        return li
    for i,el in enumerate(li):
        if i == 0:
            heapq.heappush(minH,el)
            m.append(minH[0])
        else:
            md = m[-1]
            heapq.heappush(minH,el) if el >= md else heapq.heappush(maxH,el)  # @NoEffect
        heapq.heapify(minH)
        heapq._heapify_max(maxH)
        if i > 0:
            if len(minH) == len(maxH):
                m.append((minH[0] + maxH[0])/2.0)
            elif len(minH) - len(maxH) == 1:
                m.append(minH[0])
            elif len(maxH) - len(minH) == 1:
                m.append(maxH[0])
            else:
                while abs(len(minH) - len(maxH)) != 1:
                    if len(minH) > len(maxH):
                        heapq.heappush(maxH, heapq.heappop(minH))
                    heapq.heappush(minH, heapq.heappop(maxH))
    return m

li = [5,3,4,1,6]
print medians(li)