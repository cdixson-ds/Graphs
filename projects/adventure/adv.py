from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def reverse(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'
    else:
        return None


#Create a traversal graph
traversal_graph = {}

s = Stack()
#q = Queue()

s.push(player.current_room)

#create a set to store visited vertices
visited_rooms = set()

#init reverse path
reverse_path = []

#while rooms to visit
while len(visited_rooms) < len(room_graph):

    #look at
    current_room = s.pop()

    #list of rooms not visited
    not_visited = []

    # go back if room has been visited
    if current_room.id in visited_rooms:
        if len(reverse_path) > 0:
            go_back = reverse_path.pop()
            player.travel(go_back)
            traversal_path.append(go_back)
    else:
        # push to stack
        s.push(current_room)
        # Add to traversal graph
        if current_room.id not in traversal_graph:
            traversal_graph[current_room.id] = {}
            for direction in current_room.get_exits():
                traversal_graph[current_room.id][direction] = '?'

        for key_id in traversal_graph[current_room.id]:
            if traversal_graph[current_room.id][key_id] == '?':
                not_visited.append(key_id)

        #if rooms have been visited add to visited rooms
        if len(not_visited) == 0:
            visited_rooms.add(current_room.id)
            continue

        #shuffle and visit random room
        random.shuffle(not_visited)
        player.travel(not_visited[0])
        traversal_path.append(not_visited[0])
       
        traversal_graph[current_room.id][not_visited[0]] = player.current_room.id
        if player.current_room.id not in traversal_graph:
            traversal_graph[player.current_room.id] = {}
            for direction in player.current_room.get_exits():
                traversal_graph[player.current_room.id][direction] = '?'

        traversal_graph[player.current_room.id][reverse(not_visited[0])] = current_room.id
        s.push(player.current_room)
        reverse_path.append(reverse(not_visited[0]))

        #print(traversal_graph)
        #print(traversal_path)





visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
