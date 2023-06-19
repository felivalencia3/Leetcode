#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#


# @lc code=start
class WordNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if curr.children[idx] is None:
                curr.children[idx] = WordNode()
            curr = curr.children[idx]
        curr.end = True

    def search(self, word: str) -> bool:
        if not any(self.root.children):
            return False

        def search_helper(curr: WordNode, remaining: str, level: int) -> bool:
            if level == len(word):
                return curr.end

            if not curr.children:
                return False

            c = remaining[0]
            if c == ".":
                curr_bool = False
                for i in range(26):
                    if curr.children[i] is not None:
                        curr_bool = curr_bool or search_helper(
                            curr.children[i], remaining[1:], level + 1
                        )

                return curr_bool
            else:
                next = curr.children[ord(c) - ord("a")]
                if next is not None:
                    return search_helper(
                        curr.children[ord(c) - ord("a")], remaining[1:], level + 1
                    )
                return False

        return search_helper(self.root, word, 0)


wd = WordDictionary()
wd.addWord("a")
wd.addWord("a")
print(wd.search("aa"))
print(wd.search("."))
print(wd.search("a"))
print(wd.search(".a"))
print(wd.search("a."))
