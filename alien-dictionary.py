class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # make a dictionary that maps every unique character in words to a set (to avoid dups)
        adj = {c: set() for w in words for c in w}
        
        # Go through every pair of words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            # base case: if the prefixes of word1 and word2 are equal but word1 is larger.
            if word1[:minLen] == word2[:minLen] and len(word1) > len(word2):
                return ""
            # normally, go through every character inside minLen
            # to check for first differing character
            for j in range(minLen):
                if word1[j] != word2[j]:
                    # connect the differing characters in adj list. word1[j] -> word2[j]
                    adj[word1[j]].add(word2[j])
                    break

        # Now can do DFS
        visit = {} # False = visited, True = visited and in path, None = not visited
        res = []
        # dfs function, pass in current char we are visiting
        def dfs(c: str):
            if c in visit:
                # if this returns True, thats a loop.
                return visit[c]
            visit[c] = True

            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True

            visit[c] = False
            # Post order add to res
            res.append(c)
        # Call DFS
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
