def dfs(matrix: list[list[int]]) -> None:
    # 1. check for empty graph
    if not matrix:
        return
    
    # 2. Initialize helper variables
    ROWS, COLS = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # 3. DFS recursive traverse function:
    def traverse(i, j):
        # a. check if in visited
        if (i, j) in visited:
            return
        # b. add to visited
        visited.add((i,j))

        # c. traverse neighbors
        for di, dj in directions:
            if 0 <= i + di < ROWS and 0 <= j + dj < COLS:
                # d. add in question specific checks here
                traverse(i + di, j + dj)

    # 4. Traverse each point in the matrix
    for i in range(ROWS):
        for j in range(COLS):
            traverse(i, j)
