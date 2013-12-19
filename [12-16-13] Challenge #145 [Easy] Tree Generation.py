#[12-16-13] Challenge #145 [Easy] Tree Generation
#http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/

base_size, stump, needles = 21,"=","+"

def draw_tree(base_size, stump, needles):
    levels = (base_size//2)+1
    tree = [" "*(levels-(x+1))+(needles+(needles*x*2))
            +" "*(levels-(x+1)) for x in range(levels)]
    for lev in tree:
        print (lev)
    print(" "*((base_size-3)//2)+(stump*3)+" "*((base_size-3)//2))

draw_tree(base_size, stump, needles)
