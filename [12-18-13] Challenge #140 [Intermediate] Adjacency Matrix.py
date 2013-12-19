

#[12-18-13] Challenge #140 [Intermediate] Adjacency Matrix
#http://www.reddit.com/r/dailyprogrammer/comments/1t6dlf/121813_challenge_140_intermediate_adjacency_matrix/

data = [x.strip() for x in open("challenge140I.txt").readlines()]
size, lines = int(data[0].split()[0]),int(data[0].split()[1])

rules = []
for rule in data[1:]:
    part1, part2 = rule.split(" -> ")
    subparts1, subparts2 = part1.split(), part2.split()
    for x in subparts1:
        for y in subparts2:
            rules.append((x,y))

empty_matrix = [["0"]*size for x in range(size)]

for x,y in rules:
    empty_matrix[int(x)][int(y)] = "1"

for line in empty_matrix:
    print("".join(line))











