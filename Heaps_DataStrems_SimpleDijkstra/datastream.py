import sys
import heapq

def datastream(count = False, h = [],k = 0,c = []):
    for line in sys.stdin:
        if line == "\n":
            i = 0
            while( i < k):
                var = heapq.heappop(h)
                c.append(var)
                i+=1  
            print(" ".join(map(str,c)))
            break  
        line = int(line.strip("\n"))
        if count:
            heapq.heappush(h,line)
            heapq.heapify(h)
        if count == False:
            k = line
            count = True    
        
datastream()