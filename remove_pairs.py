from typing import Optional


def solution(s: str) -> Optional[str]:
    # 1. Make freq map
    counter = {}
    for i, char in enumerate(s):
        if char not in counter:
            counter[char] = [1, [i]]
        else:
            counter[char][0] += 1
            counter[char][0] %= 2
            counter[char][1].append(i)
    counter = {key: value[1] for key, value in counter.items() if value[0] == 1}
    print(counter)
    
    def dp(word: str, choices: list, last_idx: int) -> str:
        if len(word) == len(counter.keys()):
            return word

        res = "ZZ"
        for char in choices:
            for idx in counter[char]:
                if idx > last_idx:
                    new_choices = choices.copy()
                    new_choices.remove(char)
                    res = min(res, dp(word + char, new_choices, idx))
        return res
    return dp("", list(counter.keys()), -1)

print(solution("ZYXZYZY"))
