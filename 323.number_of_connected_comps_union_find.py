# Leetcode 323

class Solution:
    def number_of_connected(self, n: int, edges: list[list[int]]) -> int:
        if not edges:
            return n
        if not n:
            return 0
        
        # Naive: do a DFS, mark as visited like number of islands. O(E + V)
        # Better: Union Find (made for this problem)
        # Hold 2 arrays, one called parent. this one holds a value for each node in input
        # par, initial = [0, 1, 2, 3, 4....] each par[i] represents node i.
        # says each node is the parent of itself.
        # as we go through each edge, we update the parent array. edge[1]'s parent will now be edge[0].
        # basically decreases number of disjoint components by 1.
        # also hold rank array, which is the "size" of that node's little subgraph, initially 1 for all.
        # after merging 0 and 1, leave 1's rank the same, increase the parent's rank. rank = [2, 1, 1...]
        # then if something wants to merge with 1, make it merge with 1's parent, 0.
        par = [i for i in range(n)]
        rank = [0] * n
        
        # want to find n1's root parent (to add n2 to it)
        def find(n1: int) -> int:
            res = n1
            while res != par[res]:
                # path compression
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1: int, n2: int) -> int:
            # find root parents of n1 and n2
            p1, p2 = find(n1), find(n2)
            # if they have the same parent, return
            if p1 == p2:
                # indicate didn't do a union
                return 0
            
            # make the one with the largest rank be the new parent of the other one, and rank++
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += 1
            else:
                par[p2] = p1
                rank[p1] += 1
            # indicate union was done, this tells us if we need to decrease subgraph count
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res

print(Solution().number_of_connected(5, [[0, 1], [1,2], [3,4]]))
