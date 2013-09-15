

#[09/11/13] Challenge #133 [Intermediate] Chain Reaction


"""
http://www.reddit.com/r/dailyprogrammer/comments/1m71k9/091113_challenge_133_intermediate_chain_reaction/
"""
import string
import copy

number, grid_size = open("challenge133inter.txt").readline().split()
elements = [x.strip().split() for x in open("challenge133inter.txt").readlines()[1:]]

grid_map = {k:v for k,v in zip([x for x in string.ascii_uppercase],[x for x  in range(25)])}

for i,e in enumerate(elements):
    e.append(string.ascii_uppercase[i])
    for c in range(3):
        e[c] = int(e[c])

grid =[[" " for x in range(int(grid_size))] for y in range(int(grid_size))]
events = []  #(xcoord, ycoord, distance_left, direction, origin letter)

def update_grid():
    for e in elements:
        grid[int(e[1])][int(e[0])]= e[4]

def display_grid(step):
    print("Step "+str(step)+":")
    for g in grid:
        line = ""
        for c in g:
            line+=c
        print(line)
    print(" ")

def update_and_display(step):
    update_grid()
    display_grid(step)

def in_grid(event):
    return event[0] >= 0 and event[1] >= 0 and event[0] < int(grid_size) and event[1] < int(grid_size)

def remove_events(element):
    if element in events:
        events.remove(element)

def add_events(element):
    x, y, dist, direction, l = element
    for e in direction:
        if e == "u":
            if in_grid([x, y-1, dist-1,e,l]) and dist > 0:
                events.append([x, y-1, dist-1,e,l])
            else:
                remove_events(element)
        if e == "d":
            if in_grid([x, y+1, dist-1,e,l]) and dist > 0:
                events.append([x, y+1, dist-1,e,l])
            else:
                remove_events(element)
        if e == "r":
            if in_grid([x+1, y, dist-1,e,l]) and dist > 0:
                events.append([x+1, y, dist-1,e,l])
            else:
                remove_events(element)
        if e == "l":
            if in_grid([x-1, y, dist-1,e,l]) and dist > 0:
                events.append([x-1, y, dist-1,e,l])
            else:
                remove_events(element)

def progress_events():
    current_events = copy.deepcopy(events)
    element_triggered = False
    for e in current_events:
        for element in elements:
            if e[0] == element[0] and e[1] == element[1] and element[4] != "X":
                add_events(element)
                element[4] = "X"
                element_triggered = True
        add_events(e)
        if e in events:
            events.remove(e)
    return element_triggered

def simulate():
    step = 0
    update_and_display(step)
    add_events(elements[grid_map["A"]])
    elements[grid_map["A"]][4] = "X"
    step+=1
    update_and_display(step)
    while events != []:
        if progress_events():
            step +=1
            update_and_display(step)

simulate()

#print(events, elements)

