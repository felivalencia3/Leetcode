def number_of_connected(n: int, edges: list[list[int]]):
    par = [i for i in range(n)]
    rank  = [1] * n

    def find(n1):
        # Find n1's root parent
        res = n1
        while res != par[res]:
            # Optimization, make parent equal to grandparent to make linked list shorter,
            par[res] = par[par[res]]
            res = par[res]
        return res
    def union(n1, n2) -> int:
        p1, p2 = find(n1), find(n2)
        
        if p1 == p2:
            return 0
        if rank[p2] > rank[p1]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = 1
            rank[p1] += rank[p2]
        return 1
    
    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res

test = [[0, 1], [1, 2], [3, 4]]
print(number_of_connected(5, test))
