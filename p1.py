from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):
  
	dist = {}
	dist[src] = 0
	prev = {}
 	prev[src] = None
	queue = [(dist[src], src)]

 	while queue:
 		node = heappop(queue)

  		if node[1] == dst:
  			break

  		neighbors = adj(graph, node)
  		for next_node in neighbors:
  			if next_node[1] not in prev or node[0] < dist[next_node[1]]:
	  			dist[next_node[1]] = node[0]        
	  			prev[next_node[1]] = node[1]
	  			heappush(queue,(next_node))
 	if node[1] == dst:

		path = []
		node = node[1]

		while node:
			path.append(node)
			node = prev[node]
		path.reverse()
		return path
	else:
		return []


def navigation_edges(level, cell):
  	steps = []
	x, y = cell[1]
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			dist = sqrt(dx*dx+dy*dy)
			if dist > 0 and next_cell in level['spaces']:

				steps.append((cell[0] + dist, next_cell))
	return steps

def test_route(filename, src_waypoint, dst_waypoint):
	level = load_level(filename)

	show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)
