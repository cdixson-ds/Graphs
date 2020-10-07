
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

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

def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    path = [starting_node]

    q.enqueue(path)

    while q.size() > 0:
        current_path = q.dequeue()
        new_path = []
        flag = False

        #loop through ancestors
        for node in current_path:
            for ancestor in ancestors:
                #compare ancestor to each node
                if ancestor[1] == node:
                    new_path.append(ancestor[0])
                    flag = True
                    q.enqueue(new_path)

        if flag is False:
            if current_path[0] == starting_node:
                return -1
            else:
                return current_path[0]


    #neighbors = {}  #key would be a node and value would be parent's tupple
    # neighbors = []

    # for a in ancestors:
    #      if a[1] == starting_node:
    #          neighbors.append(a[0])

    # return neighbors
