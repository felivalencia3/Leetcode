import time

def map_to_val(char: str):
    unicode = ord(char.lower())
    return (unicode - 96) // 3 + 1

def solution(nums: str):
    prefix = [0]
    for i in range(1, len(nums) + 1):
        prefix.append(prefix[i - 1] + map_to_val(nums[i - 1]))

    count = 0
    for start in range(len(nums)):
        extras_count = {}
        for end in range(start + 1, len(nums) + 1):
            diff = prefix[end] - prefix[start]
            substr_len = end - start
            if diff % substr_len == 0:
                if diff // substr_len not in extras_count:
                    extras_count[diff // substr_len] = 1
                count += extras_count[diff // substr_len]
                extras_count[diff // substr_len] += 1

    return count

start = time.time()
solution("asdf")
end = time.time()
exec_time = (end - start) * 1000
print("Execution time:", exec_time, "milliseconds")
