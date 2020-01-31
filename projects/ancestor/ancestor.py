from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph=Graph()
    for i in ancestors:
        for x in i:
            graph.add_vertex(x)
    for i in ancestors:
        graph.add_edge(i[0],i[1])
        # graph.add_edge(i[1],i[0])
    longest=[None]
    node=-1
    for i in graph.vertices:
        print("hi",i,graph.bfs(i,starting_node))
        if i!=starting_node and graph.bfs(i,starting_node):
            print("INSIDE",i)
            if len(graph.bfs(i,starting_node)) == len(longest):
                if i < node:
                    longest=graph.bfs(i,starting_node)
                    node=i
            if len(graph.bfs(i,starting_node)) < len(longest):
                longest=graph.bfs(i,starting_node)
                node=i
        print("Wow", i,starting_node)

    return node

        
    # print("WOOOOW",shortest)
