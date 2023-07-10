from typing import Optional


class GraphNode:
    def __init__(self, data: int, neighbors: list[object]=[]) -> None:
        self.data = data
        self.neighbors = neighbors
        
    def __str__(self) -> str:
        return f"[{self.data}]"

    def __eq__(self, __otherNode) -> bool:
        return self.data == __otherNode.value


class Graph:
    def __init__(self) -> None:
        self.nodes = []

