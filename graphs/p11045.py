from collections import defaultdict 

# This class represents a directed graph using adjacency matrix representation 
# Implementation From Geeksforgeeks.org
class Graph: 
   
    def __init__(self,graph): 
      self.graph = graph # residual graph 
      self. ROW = len(graph) 
          
    def BFS(self,s, t, parent): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
          
        # Create a queue for BFS 
        queue=[] 
          
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
           
         # Standard BFS Loop 
        while queue: 
  
            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
          
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
              
      
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 
  
num_cases = int(input())

for c in range(num_cases):
  n, m = list(map(int, input().split()))

  dim = (1+ 6 + m + 1)

  graph = [[0]*dim for i in range(dim)]
  
  # Source to t-shirts
  graph[0][1:7] = [n//6]*6

  acc_sizes = []

  # Sizes:
  # XS, S, M, L, XL, XXL
  index = {
    "XS": 1,
    "S": 2,
    "M": 3,
    "L": 4,
    "XL": 5,
    "XXL": 6
  }
  for i in range(m):
    tshirts = input().split()
    for t in tshirts:
      graph[index[t]][7+i] = 1
    graph[7+i][dim-1] = 1


  g = Graph(graph) 

  source, sink = 0, dim-1
  max_flow = g.FordFulkerson(source, sink)
  
  if max_flow == m:
    print("YES")
  else:
    print("NO")
