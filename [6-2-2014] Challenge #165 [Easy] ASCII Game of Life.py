#[6/2/2014] Challenge #165 [Easy] ASCII Game of Life
#http://www.reddit.com/r/dailyprogrammer/comments/271xyp/622014_challenge_165_easy_ascii_game_of_life/

data = [line.strip() for line in open("challenge165.txt").readlines()]
num_steps, num_col, num_row = [int(v) for v in data[0].split()]

grid = []
for v in data[1:]:
    line = []
    for letter in v:
        line.append(letter)
    grid.append(line)

def print_grid(grid):
    for line in grid:
        print("".join(line))
    print(" ")

def check_neighbors(x,y,g):
    num_live_neighbors = 0
    neighbors = [[(x+1)%(num_row),y],[(x-1)%(num_row),y],[x,(y+1)%(num_col)],[x,(y-1)%(num_col)],\
                 [(x-1)%(num_row),(y+1)%(num_col)],[(x-1)%(num_row),(y-1)%(num_col)],\
                 [(x+1)%(num_row),(y+1)%(num_col)],[(x+1)%(num_row),(y-1)%(num_col)]]
    for i,j in neighbors:
        if g[i][j] == "#":
            num_live_neighbors+=1
    if g[x][y]==".":
        if num_live_neighbors==3:
            return True
        else:
            return False
    if num_live_neighbors < 2 or num_live_neighbors > 3:
        return False
    return True

def advance(g):
    new_grid = []
    for x in range(num_row):
        new_row = []
        for y in range(num_col):
            if check_neighbors(x,y,g):
                new_row.append("#")
            else:
                new_row.append(".")
        new_grid.append(new_row)
    return new_grid

def game_of_life(n, g):
    for steps in range(n):
        g = advance(g)
        print_grid(g)

game_of_life(num_steps, grid)