from collections import deque

def wallsAndGates(rooms):
    EMPTY = 2**31 - 1
    if not rooms:
        return
    rows, cols = len(rooms), len(rooms[0])

    queue = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == EMPTY:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))

rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]
wallsAndGates(rooms)
print(rooms)
