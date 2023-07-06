# Topological Sort for the question I was never able to solve properly
# Example input
input = [
  ("A", ["B", "C"]),
  ("B", ["D"]),
  ("C", []),
  ("D", ["E"]),
  ("E", [])
]
def solution(codebases: list[tuple[str, list[str]]]) -> list[str]:
    # Convert input into graph using adjacency list map.
    graph = {}
    for codebase, dependencies in codebases:
        graph[codebase] = dependencies

    res = []
    visited = {node: False for node in graph}
    
    def post_dfs(codebase: str):
        visited[codebase] = True
        for neighbor in graph[codebase]:
            if not visited[neighbor]:
                post_dfs(neighbor)
        # Post order:
        res.append(codebase)

    for node in graph:
        if not visited[node]:
            post_dfs(node)
    return res[::-1]

print(solution(input))

