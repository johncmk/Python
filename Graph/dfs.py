'''DFS'''


def init_dfs(graph, color, time):
        for el in graph:
                color[el] = "w"
                time[el] = 0

def dfs(graph, color, time, u, timer = 1):

        if u not in graph:
                color = "b"
                return

        color[u] = "g"
        time[u] = timer

        for v in graph[u]:
                if color[v] == "w":
                       print u," -> ",v
                       dfs(graph, color, time, v, timer+1)
                elif color[v] == "g":
                        print u," -> ",v,"[BACK]"
                elif abs(time[u] - time[v]) > 1:
                        print u," -> ",v,"[FORWARD]"
                else:
                        print u," -> ",v,"[CROSS]"

        color[u] = "b"


if __name__ == "__main__":

        graph = {
                    "A": ["B"],
                    "B": ["C", "D", "E"],
                    "C": ["E"],
                    "D": ["A", "E"],
                    "E": []
                            }   

        color = {} # w:white, g:gray, b:black
        time = {}

        init_dfs(graph, color, time)
        dfs(graph, color, time, "A")
