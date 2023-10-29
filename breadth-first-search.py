#Breadth First Search uses FIFO Queue
#Nodes at the same level are visited before proceeding vertically 
#Queue keeps track of present nodes
#The Visited array keeps tracks of the nodes that have been visited 
#Whenever a node is visited, it is popped from the queue and added to the Visited array
#The program ends when the queue is empty
# Time Complexity: Worst Case-O(V+E )
 
from collections import deque

graph={
    'A':['B','C'],
    'B':['D','E','F'],
    'C':['G'],
    'D':[],
    'E':[],
    'F':['H'],
    'G':['I'],
    'H':[],
    'I':[]
}

def bfs(graph,node):
    visited=[]
    queue=deque()
    
    #root node is added to both the visited list and the queue
    visited.append(node)
    queue.append(node)

    #loop while the queue is not empty, removing the node that was first added
    while queue:
        s=queue.popleft()
        print(s,end=' ')

        #iterate through the adjacent nodes
        for n in graph[s]:
            if n not in visited:#if the adjacent node has not yet been visited, it is added to the visited list and the queue
                visited.append(n)
                queue.append(n)
bfs(graph,'A')