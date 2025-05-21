def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # Base case: Out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        # Mark as visited
        grid[r][c] = '0'
        # Visit all 4 directions
        dfs(r-1, c)  # up
        dfs(r+1, c)  # down
        dfs(r, c-1)  # left
        dfs(r, c+1)  # right

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found new island
                count += 1
                dfs(r, c)  # Sink all connected land

    return count
