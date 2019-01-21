import sys
from Queue import Queue
import heapq
from heapq import heappush, heappop

class PriorityQueue(Queue):
    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = []
    def _qsize(self, len = len):
        return len(self.queue)
    def _put(self, item, heappush = heapq.heappush):
        return heappush(self.queue, item)
    def _get(self, heappop = heapq.heappop):
        return heappop(self.queue)

def create_graph(filename):
  graph = {}
  file = open(filename, 'r')
  for line in file:
    if 'END OF INPUT' in line:
      return graph
    s, d, cost = line.rstrip().split()
    graph.setdefault(s, []).append((d, cost))
    graph.setdefault(d, []).append((s, cost))


def uniform_cost_search(graph, source, destination): 
  if source not in graph:
    print ('Source node not present in given data.')
    sys.exit()
  if destination not in graph:
    print ('Destination node not present in given data.')
    sys.exit()
  que = PriorityQueue()
  seen = set()
  path = [] 
  que.put((0, [source]))
  while que.empty() != True:
    cost, path = que.get()
    l = len(path)-1
    node = path[l]
    if node not in seen:
      seen.add(node)
      if node == destination:
        path.append(cost) 
        return path
      nodes = graph[node]
      for x in [x[0] for x in nodes]:
        if x not in seen:
          pos = [a[0] for a in graph[node]].index(x)
          sum_cost = cost + int(graph[node][pos][1])
          temp = path[:]
          temp.append(x)
          que.put((sum_cost, temp))
  if que.empty():
    print ('distance: infinity\nroute:\nnone')
    return 

def disp_path(graph,path):
  distance = path[-1]
  print ('distance: %s km'%(distance))
  print ('route: ')
  for x in path[:-2]:
    y = path.index(x)
    p = [z[0] for z in graph[x]].index(path[y+1])
    cost = graph[x][p][1]
    print ('%s to %s, %s km' %(x,path[y+1],cost))


#Get the input file, start city and destination city as command line arguments.
filename = sys.argv[1]
source = sys.argv[2]
destination = sys.argv[3]
#Split the input file into source, destination and cost between them.
#Form paths between cities that can be reached from one another.
graph = {}
graph = create_graph(filename) 
#Find the minimum cost path between the source and destination city.
path = []
path = uniform_cost_search(graph, source, destination)
#Display the path. 
if path:
    disp_path(graph,path)

