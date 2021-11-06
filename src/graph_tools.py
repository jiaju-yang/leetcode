class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.val == other.val
        return False

    def __str__(self) -> str:
        return f'Node({self.val})'

    def __repr__(self) -> str:
        return str(self)


def construct_graph_from_adj_list(adj_list):
    if not adj_list:
        return None
    nodes = {}
    for value, adj in enumerate(adj_list, 1):
        node = nodes[value] if value in nodes else Node(value)
        nodes[value] = node
        for adj_node_value in adj:
            if adj_node_value not in nodes:
                nodes[adj_node_value] = Node(adj_node_value)
            node.neighbors.append(nodes[adj_node_value])
    return nodes[1]


def is_graph_equal(node_a: Node, node_b: Node):
    if not node_a and not node_b:
        return True
    visited = set()

    def is_equal(node_a, node_b):
        if node_a.val in visited:
            return True
        if node_a != node_b or len(node_a.neighbors) != len(node_b.neighbors):
            return False
        visited.add(node_a.val)
        for adj_of_a, adj_of_b in zip(node_a.neighbors, node_b.neighbors):
            if not is_equal(adj_of_a, adj_of_b):
                return False
        return True
    return is_equal(node_a, node_b)
