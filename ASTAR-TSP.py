
class State():
	def __init__(self, n, f, g, parent):
		self.n = n
		self.f = f
		self.g = g
		self.parent = parent
	
	def __repr__(self):
		return '{}'.format(self.n)	

def heuristic(node):
	global nodes
	tempVis = []
	cost = 0
	for x in range(0, nodes):
		if x not in visited and x not in tempVis and graph[node.n][x] > 0:
			tempVis.append(x)
			cost = cost + graph[node.n][x]
	return cost			
		
# Getting input from file
def readGraph():
	global nodes
	global graph
	for x in range(0, nodes):
		temp = []
		for y in range(0, nodes):
			inp = int(input())
			temp.append(inp)
		graph.append(temp)
	print(graph)				

def stateGen(node):
	global nodes
	for x in range(0, nodes):
		if x not in visited and graph[node.n][x] > 0:
			newNode = State(x, 0, node.g + graph[node.n][x], node)
			newNode.f = newNode.g + heuristic(newNode)
			OPEN.append(newNode)

def getMin(node):
	OPEN.sort(key=lambda x: x.f, reverse=False)
	for x in OPEN:
		if(graph[node.n][x.n] > 0):
			return x

def tracePath(node):
	file = open('output.txt', 'w')
	cst = 0
	file.write('Path:')
	#print("Path:", end=" ")		
	while(node.parent != None):
		cst = cst + graph[node.n][node.parent.n]
		file.write(str(node.n+1))
		#print(node.n + 1, end=" ")
		node = node.parent
	file.write(str(node.n+1))
	#print (node.n  + 1)
	file.write(str("cost:"))
	#print("Cost:", end=" ")
	
	file.write(str(cst))
	file.close()
			
def main():
	global nodes
	nodes = int(input("Enter number of nodes: "))
	readGraph()

	iState = State(0, 0, 0, None)
	OPEN.append(iState)
	stateGen(iState)
	visited.append(0)
	
	while(True):
		if len(visited) == nodes:
			tracePath(nxtNode)
			break
		
		nxtNode = getMin(iState)
		OPEN.clear()
		visited.append(nxtNode.n)
		stateGen(nxtNode)
		iState = nxtNode

nodes = 0
graph  = []
visited = []
OPEN = []
main()