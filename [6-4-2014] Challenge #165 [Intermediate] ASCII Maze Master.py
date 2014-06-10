
data = [list(line.strip()) for line in open("challenge165I.txt").readlines()]
maze = data[1:]
cols, rows = map(int,"".join(data[0]).split())

start = ()
end = ()

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == "S":
            start = (i,j)
        if maze[i][j] == "E":
            end = (i,j)

path_start = [[start]]

def print_maze(maze):
    for row in maze:
        print ("".join(row))
    print(" ")

def find_path(maze, paths, show_paths=False):
    temp_maze = [line[:] for line in maze]

    while True:
        new_paths = []
        for path in paths:
            if show_paths:
                print_maze(temp_maze)
            i,j = path[-1]
            directions = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
            for d in directions:
                target = temp_maze[d[0]][d[1]]
                if target == "E":
                    return path
                elif target in "#*":
                    continue
                else:
                    temp_maze[d[0]][d[1]]="*"
                    new_paths.append(path+[(d[0],d[1])])
        paths = new_paths


def solve_maze(maze,path_start,show_paths=False):
    best_path = find_path(maze, path_start,show_paths)
    best_maze = [line[:] for line in maze]
    for step in best_path[1:]:
        best_maze[step[0]][step[1]]="*"
    print_maze(best_maze)
    print(best_path)

solve_maze(maze,path_start)
