#[2014-12-5] Challenge #191 [Hard] Tricky Stick Stacking
#http://www.reddit.com/r/dailyprogrammer/comments/2oe0px/2014125_challenge_191_hard_tricky_stick_stacking/

data = open("challenge191.txt").readlines()

lines = []
for i,x in enumerate(data[1:]):
    coords = x.strip().split(":")[1].split(",")
    lines.append([i+1,[float(x) for x in coords]])
    
def find_next(lines,target):
    if len(lines) < 2:
        return lines[target]
    x1,y1,x2,y2 = lines[target][1]
    if x1 == x2:
        x2+=0.000001
    xslope = (y2-y1)/(x2-x1)
    for alternate in lines:
        if alternate != lines[target]:
            a1,b1,a2,b2 = alternate[1]
            if a1 == a2:
                a2+=0.000001
            aslope = (b2-b1)/(a2-a1)       
            if (x1 <= a1 and a1 <= x2):
                if not y1+(xslope*(a1-x1)) > b1:
                    return find_next(lines,target+1)
            elif (x1 <= a2 and a2 <= x2):
                if not y1+(xslope*(a2-x1)) > b2:
                    return find_next(lines,target+1)
            elif (a1 <= x1 and x1 <= a2):
                if not b1+(aslope*(x1-a1)) < y1:
                    return find_next(lines,target+1)           
    return lines[target]

def challenge191(lines):
    solution= []
    temp_lines = lines[:]

    while len(solution) < len(lines):
        next_line = find_next(temp_lines,0)
        solution.append(next_line[0])
        temp_lines.remove(next_line)
        
    return solution

print ( challenge191(lines) )

