from typing import Optional


class GraphNode:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors else []
        self.visited = False

    def __str__(self):
        return f"{self.value} -> {[n.value for n in self.neighbors]}"

    def __repr__(self):
        return f"GraphNode({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def add_neighbor(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def remove_neighbor(self, node):
        if node in self.neighbors:
            self.neighbors.remove(node)


class Graph:
    def __init__(self, nodes=None) -> None:
        self.nodes = nodes if nodes else {}

    def __str__(self) -> str:
        return "\n".join([str(node) for node in self.nodes.values()])
        
    def __repr__(self):
        return f"Graph({self.nodes})"

    def add_node(self, node):
        if node.value not in self.nodes:
            self.nodes[node.value] = node

    def remove_node(self, node):
        if node.value in self.nodes:
            del self.nodes[node.value]
            for n in self.nodes.values():
                n.remove_neighbor(node)

    def add_edge(self, node1, node2):
        if node1.value not in self.nodes:
            self.add_node(node1)
        if node2.value not in self.nodes:
            self.add_node(node2)
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)
