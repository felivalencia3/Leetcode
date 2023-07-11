from collections import deque
import heapq

def dijkstra(graph: dict, source: str) -> tuple[dict, dict]:
    queue = [(0, source)]
    distance, visited, predecessor = {}, {}, {}
    for node in graph:
        distance[node] = float("inf")
        visited[node] = False
        predecessor[node] = None

    distance[source] = 0
    
    while queue:
        # pop next closest node from PQ
        dist, node = heapq.heappop(queue)
        # mark as visited
        visited[node] = True
        # loop neighbors of node:
        for neighbor in graph[node]:
            new_dist = dist + graph[node][neighbor]
            # update neighbor's distance value if smaller
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist

            predecessor[neighbor] = node # mark node as neighbor's predecessor
            heapq.heappush(queue, (new_dist, neighbor)) # add to queue, may get called next if smallest

    return distance, predecessor

def targeted_dijkstra(graph, source, target) -> tuple[int, list]:
    queue = [(0, source)]
    distance, visited, predecessor = {}, set(), {}
    for node in graph:
        distance[node] = float("inf")
        predecessor[node] = None

    distance[source] = 0

    while queue and target not in visited:
        dist, node = heapq.heappop(queue)
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                new_dist = dist + graph[node][neighbor]
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    predecessor[neighbor] = node
                    heapq.heappush(queue, (new_dist, neighbor))

    path = deque()
    current = target
    while current is not None:
        path.appendleft(current)
        current = predecessor[current]

    return distance[target], list(path)

if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 5, 'D': 10},
        'C': {'E': 3},
        'D': {'F': 11},
        'E': {'D': 4},
        'F': {}
    }

# Example source and target nodes
    source = 'A'
    target = 'F'

# Call the dijkstra function and print the results
    distance, path = targeted_dijkstra(graph, source, target)
    print(f"Shortest distance from {source} to {target}: {distance}")
    print(f"Shortest path from {source} to {target}: {path}")
