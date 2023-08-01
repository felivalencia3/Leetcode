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
    print(sorted(counter.keys())) 
print(solution("CBCAAXA"))
