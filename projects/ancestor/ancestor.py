from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph=Graph()
    for i in ancestors:
        for x in i:
            graph.add_vertex(x)
    for i in ancestors:
        graph.add_edge(i[0],i[1])
        # graph.add_edge(i[1],i[0])
    shortest=[None]*len(ancestors)
    node=starting_node
    for i in graph.vertices:
        print("hi",i)
        if i!=starting_node and graph.bfs(i,starting_node):
            print("INSIDE",i)
            if len(graph.bfs(i,starting_node)) == len(shortest):
                if i < node:
                    shortest=graph.bfs(i,starting_node)
                    starting_node=i
            if len(graph.bfs(i,starting_node)) < len(shortest):
                shortest=graph.bfs(i,starting_node)
                starting_node=i
        print("Wow", i,starting_node)
    if node==starting_node:
        starting_node=-1
    return starting_node

        
    # print("WOOOOW",shortest)
