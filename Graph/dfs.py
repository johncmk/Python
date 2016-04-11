'''DFS'''
def init_dfs(graph, color, time_d, time_f):
        for el in graph:
                color[el] = "w"
                time_d[el] = 0
                time_f[el] = 0

timer = 0

def dfs(graph, color, time_d, time_f, u):

        global timer
        
        if u not in graph:
                color = "b"
                return

        color[u] = "g"
        timer+=1
        time_d[u] = timer

        for v in graph[u]:
                if color[v] == "w":
                       print u," -> ",v
                       dfs(graph, color, time_d, time_f, v)
                elif color[v] == "g":
                        print u," -> ",v,"[BACK]"
                elif time_d[u] < time_d[v] and abs(time_d[u] - time_d[v]) > 1:
                        print u," -> ",v,"[FORWARD]"
                else:
                        print u," -> ",v,"[CROSS]"

        color[u] = "b"
        timer+=1
        time_f[u] = timer
        return

if __name__ == "__main__":

        graph = {
                    "A": ["B"],
                    "B": ["C", "D", "E"],
                    "C": ["E"],
                    "D": ["A", "E"],
                    "E": []
                            }
        
        color = {} # w:white, g:gray, b:black
        time_d = {} #discover time
        time_f = {} #finish time

        init_dfs(graph, color, time_d, time_f)
        dfs(graph, color, time_d, time_f, "A")


        print "Discover Time"
        for el in time_d:
                print el, " : ", time_d[el]

        print "Finish Time"
        for el in time_f:
                print el, " : ", time_f[el]



