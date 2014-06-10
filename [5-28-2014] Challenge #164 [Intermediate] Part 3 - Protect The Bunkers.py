#[5/28/2014] Challenge #164 [Intermediate] Part 3 - Protect The Bunkers (self.dailyprogrammer)
#http://www.reddit.com/r/dailyprogrammer/comments/26oop1/5282014_challenge_164_intermediate_part_3_protect/
import copy
import random

data = [row.strip() for row in open("challenge164Imap.txt").readlines()]
dimensions = (int(data[0].split()[0]),int(data[0].split()[1]))
border = [list("X"*(dimensions[0]+2))]
starting_field = border+[["X"]+list(row)+["X"] for row in data[1:]]+border

def print_field(f):
    for row in f:
        print(row)

nest_locations= {}
wall_possibilities = []

for m in range(dimensions[0]+1):
    for n in range(dimensions[1]+1):
        if starting_field[m][n] == "*":
            nest_locations[(m,n)]=False
        if starting_field[m][n] == '-':
            wall_possibilities.append((m,n))

def spread_termites(nest_locs, field):
    bunker_reached=False
    new_nests = {}
    for nest,used in nest_locs.items():
        m,n = nest
        possibs = {"left":(m,n-1) ,"right":(m,n+1) , "up":(m-1,n), "down":(m+1,n)}
        for vals in possibs.values():
            target = field[vals[0]][vals[1]]
            if target in "+-":
                new_nests[vals] = False
                field[vals[0]][vals[1]] = "*"
            if target == 'o':
                bunker_reached=True
        nest_locs[nest] = True
    return (bunker_reached,new_nests)

def fully_propagate(field):
    fully_spread = False
    nest_locs = copy.deepcopy(nest_locations)
    bunker_hit = False
    while not fully_spread:
        bunker_hit, new_nests = spread_termites(nest_locs, field)
        if bunker_hit or len(new_nests)==0:
            fully_spread = True
        else:
            for nest, v in new_nests.items():
                nest_locs[nest]=v
    return bunker_hit

def make_walls(field,num_walls):
    random.shuffle(wall_possibilities)
    wall_positions = wall_possibilities[0:num_walls]
    for wall in wall_positions:
        field[wall[0]][wall[1]] = "@"
    return field

def wall_heuristic(runs):
    for num_walls in range(1,len(wall_possibilities)+1):
        for run in range(runs):
            blank_field = copy.deepcopy(starting_field)
            random_field = make_walls(blank_field,num_walls)
            bunker_hit = fully_propagate(random_field)
            if bunker_hit == False:
                print("Solution found!")
                print_field(random_field)
                print(num_walls)
                return

wall_heuristic(1000)




