'''BFS to directed graph O(n+m)
    Determine whether the graph is bipartite
    while traversing the graph with using BFS
    if there exists same color of parent node and child node then
    the graph is bipartite
'''


def init_bfs(level, graph, q):
    for i, el in enumerate(graph):
        if i == 0:
            q.append(el) # enqueue first node of graph
            level[el] = 0 # Start node stars from zero level.
        else:
            level[el] = -1


def bfs(level, graph, q):

    path = ""
    cross = []
    back = []
    
    while q != []:
        u = q.pop(0)
        path = path + u + " "
        for v in graph[u]:
            if level[v] == -1:
                level[v] = level[u] + 1
                q.append(v)
            elif level[v] < level[u]:
                back.append(u + "->" + v)
            else:
                cross.append(u + "->" + v)

    print "PATH : ", path
    print "BACK : ", back
    print "CROSS : ", cross


if __name__ == "__main__":

    graph = {
            "A": ["B"],
            "B": ["C", "D", "E"],
            "C": ["E"],
            "D": ["A", "E"],
            "E": []
                            }

    level = {}
    q = []

    init_bfs(level, graph, q)
    bfs(level, graph, q)
    
    print "FORWARD : forward edge does not exists in BFS because BFS edge doesn allow any precedessor between u->v"
