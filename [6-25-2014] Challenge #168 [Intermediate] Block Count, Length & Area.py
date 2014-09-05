#[6/25/2014] Challenge #168 [Intermediate] Block Count, Length & Area
#http://www.reddit.com/r/dailyprogrammer/comments/291x9h/6252014_challenge_168_intermediate_block_count/

map = [list(x.strip()) for x in open("challenge168I.txt")]
dimX, dimY = len(map),len(map[0])

totals_dict = {k:{"area":0,"circumference":0,"blocks":0}\
               for k in set([tile for row in map for tile in row])}

def print_results(totals_dict):
    for k,v in totals_dict.items():
        print(k,v)

explored = []

def find_block(map):
    for x in range(dimX):
        for y in range(dimY):
            if (x,y) not in explored:
                block_segments = [(x,y)]
                block_type = map[x][y]
                block_area = 100
                block_circumference = 0
                for segment in block_segments:
                    if segment not in explored:
                        explored.append(segment)
                        new_s,p_increase = extend_block(segment[0],\
                                           segment[1],block_type,block_segments)
                        block_area+=(new_s*100)
                        block_circumference+=p_increase
                return(block_type, block_area, block_circumference)
    return False

def extend_block(x,y,block_type,block_segments):
    neighbors = find_neighbors(x,y)
    new_segments = 0
    perimeter_increase = 40
    for x2,y2 in neighbors:
        if 0 <= x2 <= dimX-1 and 0 <= y2 <= dimY-1:
            neighbor= map[x2][y2]
            if neighbor == block_type and (x2,y2) not in block_segments:
                block_segments.append((x2,y2))
                new_segments+=1
                new_segment_neighbors= find_neighbors(x2,y2)
                for x3,y3 in new_segment_neighbors:
                    if (x3,y3) in block_segments:
                        perimeter_increase-=20
    return (new_segments,perimeter_increase)

def find_neighbors(x,y):
    return [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]

def solve_map(map,totals_dict):
    while True:
        block_info = find_block(map)
        if block_info is False:
            return totals_dict
        else:
            totals_dict[block_info[0]]["area"]+=block_info[1]
            totals_dict[block_info[0]]["circumference"]+=block_info[2]
            totals_dict[block_info[0]]["blocks"]+=1

print_results(solve_map(map,totals_dict))

