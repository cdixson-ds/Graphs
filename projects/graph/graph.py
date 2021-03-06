"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
 
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        #keys are all verts in the graph, values are sets of adj verts
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph. #new, unconnceted vert
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        #v1 = from, v2 = to
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        #Init:
        q.enqueue(starting_vertex)

        #while queue isn't empty
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                #visit the node
                print(v) 
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()

        #init
        s.push(starting_vertex)

        #while queue isn't empty
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                #visit node
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        print(starting_vertex)
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        # Create a Set to store visited vertices
        visited = set()

        #Init not just starting node but the whole path
        q.enqueue([starting_vertex])

		
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
            #end of path node
            v = path[-1]
			# Grab the last vertex from the PATH / target vertex
            if v == destination_vertex:
                return path  #Found
            #if not in visited
            elif v not in visited:
                #visit node
                print(v)
                visited.add(v)
                print(v)
                # Mark it as visited...
                visited.add(v)
                #enqueue all the neighbors
                for neighbor in self.get_neighbors(v): 
                    #path to the neighbor + path to v, use * to unpack the list
                    new_path = [*path, neighbor]
                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):  #switch to stack
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

         # Create an empty queue and enqueue A PATH TO the starting vertex ID
        s = Stack()
        # Create a Set to store visited vertices
        visited = set()

        #Init:
        s.push([starting_vertex])
		
		# While the queue is not empty...
        while s.size() > 0:
			# Dequeue the first PATH
            path = s.pop()
            v = path[-1]
			# Grab the last vertex from the PATH
            if v == destination_vertex:
                return path
            #if not in visited
            elif v not in visited:
                #visit node
                print(v)
                visited.add(v)
                print(v)
                # Mark it as visited...
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    #use * to unpack the list
                    new_path = [*path, neighbor]
                    s.push(new_path)


    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = [starting_vertex]

        print(starting_vertex)
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == target_vertex:
                    return new_path

                #not returning path, path is none
                dfs_path = self.dfs_recursive(neighbor, target_vertex, visited, new_path)
                print(dfs_path)
                if dfs_path is not None:
                    return dfs_path

        return None
    

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
