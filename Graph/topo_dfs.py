
color = {"CS10" : 0, "CS11": 0, "CS20" :0, "CS21" : 0, "CS12" : 0, "CS30":0}

graph = {"CS10": ["CS11", "CS20"],
         "CS11": ["CS21"],
         "CS20": ["CS30"],
         "CS21": ["CS12", "CS20"],
         "CS12": ["CS30"],
         "CS30": []
         }

in_degree ={"CS10" : 0, "CS11": 0, "CS20" :0, "CS21" :0, "CS12" : 0, "CS30":0}
path = "CS10"

def init_dfs():
        global graph
        for x in graph:
                for y in graph[x]:
                        in_degree[y]+=1 



def dfs(head):
	color[head] = 1
	if head not in graph:
		color[head] = 2
		return 
	for x in graph[head]:
		in_degree[x]-=1
		if color[x] == 0 and in_degree[x]==0:  
			global path
			path = path + " -> " + x
			dfs(x)
	
	
	color[head] = 2
	return

if __name__ == "__main__":

        init_dfs()
        dfs("CS10")
        print path
