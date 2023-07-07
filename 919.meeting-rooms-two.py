def meeting_rooms_two(intervals: list[list[int]]) -> int:
    start, end = [], []
    for i in intervals:
        start = i.start
        end = i.end
    start.sort()
    end.sort()

    res, count = 0,0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            # A meeting started
            s += 1
            count += 1
            res = max(res, count)
        else:
            # A meeting ended
            e += 1
            count -= 1
    return res
