mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G','H'],
    'edges': [
        (8,'A','B'),
        (10,'A','G'),
        (15,'A','H'),
        (9,'B','H'),
        (11,'B','C'),
        (3,'C','H'),
        (8,'C','D'),
        (8,'C','E'),
        (7,'D','E'),
        (4,'D','F'),
        (12,'E','H'),
        (5,'E','F'),
        (3,'C','H'),
        (2,'F','G'),
        (1,'G','H'),
    ]
}

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    for node in graph['vertices']:
        make_set(node)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
            print(mst)

if __name__ == "__main__":
    kruskal(mygraph)