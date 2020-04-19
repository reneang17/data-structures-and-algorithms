import heapq



class A_star_planer(object):
    """
    Author: Rene Angeles
    My implemenation of the A* algorithm with time complexity O(n log(n)) where n is the number of nodes in the map.
    I took my inspiration from the following heap implemenation of Dijkstra algorithm:
    https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/238116/Python-Simple-Dijkstra
    """
    
    def __init__(self, map):
        """
        args: map
        Given a map, the map gets the intersections, {0 : coords_0, 1: coords_1 ...},
        and roads, a list where entry i has the conextions of node i. 
        """
        self.intersections= map.intersections
        self.roads = map.roads
        
    def distance(self, node_a, node_b):
        """
        Calcultes the euclidead distance between two nodes
        args:
        node_a: node (int)
        node_b: node (int)
        """
        cords_a = self.intersections[node_a]
        cords_b = self.intersections[node_b]
        zipped = zip(cords_a,cords_b)
        return (sum((a-b)**2 for a,b in zipped ))**0.5


    def shortest_path(self, start, goal):
        """
        Method. Calculates short path define according to the A* algorithm. 
        It uses a heap to do search insert and search on O(n log(n))).
        As a reference to this problem lo
        args:
        start: departure node (int)
        goal: destination node (int)
        """
        
        cost_heap = list() # head keeps track of the total cost
        heapq.heappush(cost_heap, (0 + self.distance(start, goal), start)) 
        
        routes = {start: None} # Dict of key-value pairs node: prev_node for each explored path 
        path_cost = {start: 0}# Dict to keep cost of each route

        while cost_heap:
           
            _ , curr_node = heapq.heappop(cost_heap) #pop node with least cost

            if curr_node == goal: # Stop when 1) reach goal, 2) curr_node cost is the least on heap. 
                break

            for next_node in self.roads[curr_node]:
                dist_start_next = path_cost[curr_node] + self.distance(curr_node, next_node)
                
                # Either for a new node or if a shorter route to a previous node is found
                # define path_cost, append route and push into heap the total cost.
                if next_node not in path_cost or dist_start_next < path_cost[next_node]:
                    path_cost[next_node] = dist_start_next
                    routes[next_node] = curr_node
                    # KEY STEP: total cost is equal to path_cost + distance to goal!
                    total_cost = path_cost[next_node] + self.distance(next_node, goal)
                    heapq.heappush(cost_heap,(total_cost , next_node))
        
        return self.trace_route(routes, start, goal)


    def trace_route(self, routes, start, goal):
        """
        Method to trace back short path found by A*
        args:
        start: node (int)
        goal: node (int)
        routes: dict with key-value pairs corresponding to next_node: node.
        returns:
        path: list of shortest path found between start and goal.
        """
        curr = goal
        path = [curr]
        while curr != start:
            curr = routes[curr]
            path.append(curr)
        path.reverse()
        return path


def shortest_path(M, start, goal):
    """
    args:
    M: map, see jupyter notebook
    start: node (int)
    goal: node(int)
    returns:
    path: short path obtaiend using the A_star_planer class
    """
    a_star_planer = A_star_planer(M)
    path = a_star_planer.shortest_path(start, goal)
    return path
