#Depth First Search traverses a graph vertically and makes use of a Stack
#Stack keeps track of present nodes
#The Visited array keeps tracks of the nodes that have been visited 
#let us add the rightmost node of the graph to the stack first so we can traverse all the nodes on the left
#Time Complexity: O(V+E)

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

def dfs(graph,node):
    visited=[]
    stack=[]

    #root node added to both the visited list and the stack
    visited.append(node)
    stack.append(node)

    #loop while the stack is not empty
    while stack:
        s=stack.pop()
        print(s,end=' ')

        #iterate through the adjacent nodes
        for n in reversed(graph[s]): #reversed function adds the rightmost node into the stack first i.e it is visited last
            if n not in visited: #if the adjacent node has not yet been visited, it is added to the visited list and the stack
                visited.append(n)
                stack.append(n)
dfs(graph,'A')

