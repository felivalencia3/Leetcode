class TrieNode:
    def __init__(self, char="", end=False, children={}) -> None:
        self.char = char
        self.end = end
        self.children = children


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        def insert_helper(curr: TrieNode, remaining: str) -> None:
            if remaining:
                c = remaining[0]
                if c not in curr.children:
                    curr.children[c] = TrieNode(c, len(remaining) == 1, {})
                else:
                    curr.children[c].end = len(remaining) == 1
                insert_helper(curr.children[c], remaining[1:])

        insert_helper(self.root, word)

    def search(self, word: str) -> bool:
        def search_helper(curr: TrieNode, remaining: str) -> bool:
            if not remaining:
                return curr.end

            c = remaining[0]
            if c in curr.children:
                return search_helper(curr.children[c], remaining[1:])
            return False

        return search_helper(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        def startsWith_helper(curr: TrieNode, remaining: str) -> bool:
            if not remaining:
                return True

            c = remaining[0]
            if c in curr.children:
                return startsWith_helper(curr.children[c], remaining[1:])
            return False

        return startsWith_helper(self.root, prefix)
