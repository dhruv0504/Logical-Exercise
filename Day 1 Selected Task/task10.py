def orangesRotting(grid):
    q = []
    time = 0 
    fresh = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r,c])
    # print(fresh)
    # print(q)

    dir = [[0,1],[0,-1],[1,0],[-1,0]]   

    while q and fresh>0:
        for i in range(len(q)):
            print(q)
            r,c = q.pop()
            for dr, dc in dir:
                row , col = dr + r, dc + c
                if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                q.append([row,col])
                fresh -= 1
        time += 1
    return time if fresh ==0 else -1

print(orangesRotting( [[2,1,1],[1,2,0],[0,1,1]]))