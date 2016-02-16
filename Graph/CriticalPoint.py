from _collections import defaultdict

graph = {'A':['B','C','H'],
         'B':['A','D'],
         'C':['A','D'],
         'D':['B','C','E','F'],
         'E':['D','F','G'],
         'F':['D'],
         'G':['E'],
         'H':['A']}

discover = {}
back = defaultdict(int)
finishTime = {}
timestamp = 1

def dfs(v, parent):
    global timestamp
    discover[v] = timestamp
    timestamp += 1
    back[v] = discover[v] #Base
    for u in graph[v]:
        if u != parent:
            if u in discover: # back edge
                back[v] = min(back[v],discover[u])
            else:
                dfs(u,v) # recursively visit child u
                back[v] = min(back[v],back[u])
    finishTime[v] = timestamp
    timestamp += 1 # finish time
    
dfs('A',None)
print "start: ",discover   
print "back: ",back.viewitems() 
print "finish: ",finishTime