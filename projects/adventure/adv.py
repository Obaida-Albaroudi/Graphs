from room import Room
from player import Player
from world import World
from util import Stack, Queue
from social import SocialGraph
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n',"s","e"]
traversal_path = []


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


# def function():
#     for i in player.current_room.get_exits():
#         if player.travel(direction).current_room.id not in visited_rooms:
#             count+=1
#     if count==0:
#         Go back to the last stored room
#     for i in player.current_room.get_exits():
#         while player.travel(i):

    

# for i in visited_rooms:
#     print(i)
# # `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)`
# def bfs(starting_id, questionMark):
#         queue = Queue()
#         queue.enqueue([starting_id])
#         visited = set()
#         while queue.size() > 0:
#             path = queue.dequeue()
#             vertex = path[-1]
#             if vertex not in visited:
#                 if vertex == questionMark:
#                     return path
#                 visited.add(vertex)
#                 for next_vert in player.current_room.get_exits():
#                     new_path = list(path) 
#                     new_path.append(next_vert)
#                     queue.enqueue(new_path)

# print(bfs(player.current_room, "?"))
for i in player.current_room.get_exits():
        traversal_path.append(i)
        while player.travel(i):
            traversal_path.append(i)
            
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
for i in world.rooms:    
    print(i)
# for i in player.current_room.get_exits():
#     print(i)
#     player.travel(i)
#     print(player.current_room,player.current_room.get_exits())
    # traversal_path.append(i)
    
# for i in visited_rooms:
#     print(i)
   

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
#         print("WOOOW",visited_rooms)
#         break
#     else:
#         print("I did not understand that command.")
