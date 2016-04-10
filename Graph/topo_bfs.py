graph = {"CS10" : ["CS11", "CS20"], "CS11" : ["CS21"], "CS20": ["CS30"], "CS21": ["CS12", "CS20"], "CS12":["CS30"],"CS30":[]}
level = {"CS10" : 0, "CS11": -1, "CS20" :-1, "CS21" : -1, "CS12" : -1, "CS30":-1}
in_degree ={"CS10" : 0, "CS11": 0, "CS20" :0, "CS21" :0, "CS12" : 0, "CS30":0}
back = []
cross = []
q = ["CS10"]
path = ""


def init_bfs():
    global graph

    for u in graph:
        for v in graph[u]:
            in_degree[v]+=1


def bfs():
    while q != []:
        u = q.pop(0)
        global path

        if path is "":
            path = path + u
        else:
            path = path + " -> " + u

        for v in graph[u]:
            in_degree[v] -= 1

            if level[v] == -1 and in_degree[v] == 0:
                q.append(v)
                level[v] = level[u] + 1




if __name__ == "__main__":

    init_bfs()
    bfs()
    print path
