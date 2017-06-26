#!/usr/bin/python
from collections import defaultdict
from priodict import priorityDictionary

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.weights = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, weight):
    #DAG 
    self.edges[from_node].append(to_node)
    #self.edges[to_node].append(from_node)
    self.weight[(from_node, to_node)] = weight


def dijkstra(graph, start, end=None):
  #Initialization   
  D = {}
  P = {}
  Q = priorityDictionary()
  Q[start] = 0
  visited = {initial: 0}
  path = {}
  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

def main():
  print "hellp"
  g= Graph()
  g.add_node('0'); g.add_node('3'); g.add_node('5'); g.add_node('9'); g.add_node('11')
  g.add_edge('0','3',3); g.add_edge('0','5',5); g.add_edge('3','5',2); g.add_edge('5','3',1)
  g.add_edge('3','9',6); g.add_edge('5','9',4); g.add_edge('9','11',2); g.add_edge('11','9',7)
  g.add_edge('5','11',6); g.add_edge('11','0',3)
  print "g.edges[0] = {}".format(g.edges['0'])
  visited0, path0 = dijkstra(g, '11')
  print visited0, path0 

if __name__ == "__main__":
  main()
       
        
