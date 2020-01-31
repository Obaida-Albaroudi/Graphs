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
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
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

# Maybe create graph
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = {}
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist, and a connection from v1 to v2
        """

        self.vertices[v1]=(v2)
    
        # if v1 in  self.vertices and v2 in self.vertices:
        #     self.vertices[v1].add(v2)
        # else:
        #     raise IndexError("That vertex does not exist!")
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if len(self.vertices)<=1:
            self.add_vertex(starting_vertex)
            objects={}
            for i in player.current_room.get_exits():
                objects[i]="?"    
            self.add_edge(player.current_room.id,objects)
        if visited is None:
            visited=set()
        # print("ON Top")
        visited.add(starting_vertex)
        # print(starting_vertex, self.vertices,self.vertices[starting_vertex])
        for child_vert in self.vertices[starting_vertex]:
            traversal_path.append(child_vert)
            print(child_vert,starting_vertex, self.vertices,visited)
            while "?" not in self.vertices[starting_vertex].values():
                
                if len(self.vertices[starting_vertex].values())<=1:
                    player.travel(child_vert)
                elif child_vert=="n":
                    player.travel("s")
                elif child_vert=="s":
                    player.travel("n")
                elif child_vert=="e":
                    player.travel("w")
                elif child_vert=="w":
                    player.travel("e")
                self.dft_recursive(player.current_room.id, visited)
            print("Top",child_vert,player.current_room.id)
            player.travel(child_vert)
            print(child_vert,player.current_room.id)
            if player.current_room.id not in visited:
                print("HERE",child_vert,starting_vertex,visited)
                if player.current_room.id not in self.vertices[starting_vertex].values():
                    self.add_vertex(player.current_room.id)
                    obj={}
                    for i in player.current_room.get_exits():
                        obj[i]="?"    
                    self.add_edge(player.current_room.id,obj)
                    obj={}
                    if child_vert=="n":
                        print("n",player.current_room.id, child_vert, starting_vertex)
                        self.vertices[starting_vertex][child_vert]=player.current_room.id
                        self.vertices[player.current_room.id]["s"]=starting_vertex
                    elif child_vert=="s":
                        print("s",player.current_room.id, child_vert, starting_vertex)
                        self.vertices[starting_vertex][child_vert]=player.current_room.id
                        self.vertices[player.current_room.id]["n"]=starting_vertex
                    elif child_vert=="e":
                        print("e",player.current_room.id, child_vert, starting_vertex)
                        self.vertices[starting_vertex][child_vert]=player.current_room.id
                        self.vertices[player.current_room.id]["w"]=starting_vertex
                    elif child_vert=="w":
                        print("w",player.current_room.id, child_vert, starting_vertex)
                        self.vertices[starting_vertex][child_vert]=player.current_room.id
                        self.vertices[player.current_room.id]["e"]=starting_vertex

                    self.dft_recursive(player.current_room.id, visited)
                    print("visited",visited)
    def dfs_recursive(self, starting_vertex, target_value,visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited=set()
        if path is None:
            path=[]
        visited.add(starting_vertex)
        path=path+[starting_vertex]
        if starting_vertex==target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path=self.dfs_recursive(child_vert, target_value,visited,path)
                if new_path:
                    return new_path
        return None
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        shortest=[None]*len(self.vertices)
        # variable=0
        queue=Queue()
        queue.enqueue([user_id])
        while queue.size()>0:
            path=queue.dequeue()
            print("path",path)
            current_user = path[-1]
            print("current_user", current_user)
            if current_user not in visited:
                print("visited", visited)
                visited[current_user]=path

                if len(visited[current_user])<len(shortest) and len(visited[current_user])>1:
                    shortest=visited[current_user]
                for ID in self.vertices[current_user]:
                    if type(ID) ==int:
                        new_path=list(path)
                        new_path.append(ID)
                        queue.enqueue(new_path)
                    
        del visited[user_id]
        print("shortest",shortest)
        return visited

graphs=Graph()

graphs.dft_recursive(player.current_room.id)

print("HI",player.current_room.id)
# graphs.vertices[0]["n"]=2
# graphs.add_edge(player.current_room.id,5)
print(graphs.vertices)
# print(graphs.get_all_social_paths(0))s
# def dfs():


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
#         print("WOOOW",visited_rooms)
#         break
#     else:
#         print("I did not understand that command.")
