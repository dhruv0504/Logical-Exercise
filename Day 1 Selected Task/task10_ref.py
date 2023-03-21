def cont(grid):
    dir =[[0,1],[0,-1],[1,0],[-1,0]]  
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                for dr, dc in dir:
                    row , col = dr + i, dc + j
                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2

def is_all_cont(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return False
    return True
            
def are_state_same(og,ng):
    if og == ng:
        return True
    else:
        return False

def steps(grid):
    step = 0
    while(True):
        ns = cont(grid)
        step += 1
        if (is_all_cont(ns)):
            return step
        if (are_state_same(ns,grid)):
            return step
        grid = ns


print(steps([[2,1,1],[1,1,0],[0,1,1]]))