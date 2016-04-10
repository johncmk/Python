'''If there is BACK edge in a graph, then there is a cycle.
    print all cycles in the graph
'''


def init_dfs(graph, color, time, pi):
    for u in graph:
        pi[u] = ""
        color[u] = "w"
        time[u] = 0


def dfs(graph, color, time, pi, u, cycle, timer = 1, no_cycle = 1):

    if u not in graph:
        color[u] = "b"
        return

    color[u] = "g"
    time[u] = timer

    for v in graph[u]:
        if color[v] == "w":
            pi[v] = u
            dfs(graph, color, time, pi, v, cycle, timer+1, no_cycle)
        elif color[v] == "g":
            cycle[no_cycle] = dfs_cycle(u,v)
            no_cycle+=1

    color[u] = "b"
    return cycle


def dfs_cycle(u,v):
    stk = [v,u]

    parent = pi[u]
    while v != parent:
        stk.append(parent)
        parent = pi[parent]
                
    stk.append(v)

    return stk

        
if __name__ == "__main__":

    graph ={
            "A": ["B"],
            "B": ["C", "D", "E"],
            "C": ["E"],
            "D": ["A", "E"],
            "E": []
                    }

    color = {}
    time = {}
    pi = {} #parent
    cycle = {}
    
    init_dfs(graph, color, time, pi)
    result = dfs(graph, color, time, pi, "A", cycle)


    if len(result) == 0:
        print "ACYCLIC"
    else:
        for el in result:
            stk = result[el]
            print el," : ",
            while stk != []:
                print stk.pop()," ",
            print 
    

