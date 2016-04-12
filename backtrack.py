graph = {'A': set(['B', 'C', 'D']),
	 'B': set(['E', 'F']),
	 'C': set(['F', 'G']),
	 'D': set([]),
	 'E': set(['H', 'I']),
	 'F': set(['J']),
	 'G': set([]),
	 'H': set([]),
	 'I': set([]),
	 'J': set([])}

graph2 = {'A': set(['B', 'C', 'D']),
	 'B': set(['E', 'F']),
	 'C': set(['G', 'H']),
	 'D': set(['I', 'J']),
	 'E': set(['K', 'L']),
	 'F': set(['L', 'M']),
	 'G': set(['N']),
	 'H': set(['O', 'P']),
	 'I': set(['P', 'Q']),
	 'J': set(['R']),
	 'K': set(['S', 'F']),
	 'L': set(['T']),
	 'M': set([]),
	 'N': set([]),
	 'O': set([]),
	 'P': set(['U']),
	 'Q': set([]),
	 'R': set([]),
	 'S': set([]),
	 'T': set([]),
	 'U': set([])}

def depth_first_search(graph, start, goal):
	openList = [start]
	closedList = []
	while len(openList) != 0:
		X = openList[0]
		print("X is: " + X)
		del openList[0]
		if X == goal:
			return "SUCCESS"
		else:
			children = sorted(graph[X])
			print("children: ")
			print(children)

			if X in openList or X in closedList:
				children = []
			else:
				closedList.insert(0, X)
				print("closed: ")
				print(closedList)

			children = [x for x in children if x not in closedList]
			openList = children + openList
			print("new open: ")
			print(openList)

	return "FAIL"

def backtrack(graph, Start, goal):
	SL = [Start]
	NSL = [Start]
	DE = []
	CS = Start
	while len(NSL) != 0:
		if CS == goal:
			return SL
		if (len(graph[CS]) == 0) and (CS not in DE):
			while len(SL) != 0 and CS == SL[0]:
				DE.insert(0, CS)
				del SL[0]
				del NSL[0]
				CS = NSL[0]
			SL.insert(0, CS)
		else:
			children = sorted(graph[CS])
			children = [x for x in children if x not in DE]
			children = [x for x in children if x not in SL]
			children = [x for x in children if x not in NSL]
			NSL = children + NSL;
			CS = NSL[0]
			SL.insert(0, CS)
	return "FAIL"

def recur(graph, current, goal, closed):
	if current == goal:
		return 0
	closed.insert(0, current)
	children = sorted(graph[current])
	while len(children) > 0: # len(children) != 0	children not in closed
		child = children[0]
		if child in closed:
			child = children[1]
		print("child: " + child)
		del children[0]
		if child not in closed:
			if recur(graph, child, goal, closed) == 0:
				print(current)
				print(closed)
				print("child: " + child)
				return "SUCCESS2"
	return "FAIL"
	
#print(depth_first_search(graph, 'A', 'G'))
#print(recur(graph, 'A', 'B', []))
print(backtrack(graph, 'A', 'G'))