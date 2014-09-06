"""
project for week 1
For your first project, you will write Python code that creates dictionaries corresponding to some simple examples of graphs.
You will also implement two short functions that compute information about the distribution of the in-degrees for nodes in these graphs. You will then use these functions in the Application component of Module 1 where you will analyze the degree distribution of a citation graph for a collection of physics papers.
This final portion of module will be peer assessed.
"""

# Directed graphs
EX_GRAPH0 = {
    0: set([1,2]),
    1: set(),
    2: set()
}

EX_GRAPH1 = {
    0: set([1,4,5]),
    1: set([2,6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set()
}

EX_GRAPH2 = {
    0: set([1,4,5]),
    1: set([2,6]),
    2: set([3,7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set([]),
    7: set([3]),
    8: set([1,2]),
    9: set([0,3,4,5,6,7])
}


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with the specified number of nodes.
    self-loops are not allowed
    """
    graph = {}
    for node in xrange(num_nodes):
        connected_nodes = range(num_nodes)
        # remove self-loops in nodes
        connected_nodes.remove(node)
        graph[node] = set(connected_nodes)
    return graph


def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph
    """
    in_degrees = {}
    for key in digraph.keys():
        number_of_occurrence = 0
        for set_ in digraph.values():
            number_of_occurrence += list(set_).count(key)
        in_degrees[key] = number_of_occurrence
    return in_degrees


def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution
    of the in-degrees of the graph.
    The function should return a dictionary whose keys correspond to in-degrees of nodes in the graph.
    The value associated with each particular in-degree is the number of nodes with that in-degree.
    """
    deg_distr = {}
    in_degrees = compute_in_degrees(digraph).values()
    for degree in in_degrees:
        if degree in deg_distr:
            continue
        else:
            deg_distr[degree] = in_degrees.count(degree)
    return deg_distr