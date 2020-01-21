from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    count=1
    graph=Graph()
    for i in ancestors:
        graph.add_vertex(i[0])
    print(graph.vertices)
    for i in ancestors:
        graph.add_edge(i[0],i[1])
    print(graph.dfs(1, 10))
