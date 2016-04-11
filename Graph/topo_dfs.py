'''Topological sort in DFS'''

'''Global variables'''
timer = 0
no_topo = False
ll = [] #LinkedList

def init_dfs(graph, color, time_d, time_f):
        for el in graph:
                color[el] = "w"
                time_d[el] = 0
                time_f[el] = 0



def dfs(graph, color, time_d, time_f, u):
        global timer
        global no_topo
        global ll
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
                        no_topo = True
                elif time_d[u] < time_d[v] and abs(time_d[u] - time_d[v]) > 1:
                        print u," -> ",v,"[FORWARD]"
                else:
                        print u," -> ",v,"[CROSS]"

        color[u] = "b"
        timer+=1
        time_f[u] = timer
        ll.insert(0,u)
        return

def print_topo(time_f):
    rev_f = {}
    li = []

    for el in time_f:
        t = time_f[el]
        rev_f[t] = el
        li.append(t)

    li = sorted(li)

    for el in reversed(li):
        k = el
        print rev_f[k]," ",
    
            
if __name__ == "__main__":

        graph = {
                "CS10": ["CS20", "CS11"],
                "CS11": ["CS21"],
                "CS20": ["CS30"],
                "CS21": ["CS20", "CS12"],
                "CS12": ["CS30"],
                "CS30": []
                }
        
        color = {} # w:white, g:gray, b:black
        time_d = {} #discover time
        time_f = {} #finish time

        init_dfs(graph, color, time_d, time_f)
        dfs(graph, color, time_d, time_f, "CS10")

        if no_topo == True:
            print "NO TOPOLOGICAL ORDER"
        else:   #2 way to print the topo order.
            #1 print by reversed finish time
            print_topo(time_f)
            #2 simply output the linkedlist list
            #print ll



