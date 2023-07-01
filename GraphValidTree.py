from collections import defaultdict

def graph_valid_tree(n: int, edges: list[int]):
    # 1) Build adjacency list
    visited = set()
    adj_list = defaultdict(list)
    for n1, n2 in edges:
        adj_list[n1] += [n2]
        adj_list[n2] += [n1]

    def dfs(curr: int, prev: int) -> bool:
        if curr in visited:
            return False

        visited.add(curr)
                
        for next in adj_list[curr]:
            if next != prev:
                if not dfs(next, curr):
                    return False
        return True
    
    return dfs(0, None) and len(visited) == n

            

test = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(graph_valid_tree(5, test))
