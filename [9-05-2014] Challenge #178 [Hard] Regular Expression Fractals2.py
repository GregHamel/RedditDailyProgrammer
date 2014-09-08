#[9/05/2014] Challenge #178 [Hard] Regular Expression Fractals
#http://www.reddit.com/r/dailyprogrammer/comments/2fkh8u/9052014_challenge_178_hard_regular_expression/

import re, math

size = 256

tree_fractal = r'.*(13|31|24|42).*'
triangle_fractal = r'.*1.*'
square_fractal = r'.*(13|31).*'
ex1 = r'[13][24][^1][^2][^3][^4]'

base_board = ["2","1","3","4"]

def expand_base(size):
    size_factor = int(math.log(size**2,4)-1)
    board = base_board[:]
    for factor in range(size_factor):
        next = []
        for cell in base_board:
            for c2 in board:
                next.append(cell+c2)
        h1 = next[0:(len(next)//2)]
        h2 = next[(len(next)//2):]
        h3 = []
        h4 = []
        divisions = int(2**(1+factor))
        for row in range(divisions):
            for group in range(2):
                h3+= h1[((group*divisions)**2)+row*divisions:((group*divisions)**2)+row*divisions+divisions]
                h4+= h2[((group*divisions)**2)+row*divisions:((group*divisions)**2)+row*divisions+divisions]
        board = h3+h4
    return board

board = expand_base(size)

def print_board_fractal(b,exp,size):
    fractal = ""
    for cell in b:
        if re.match(exp, cell):
            fractal+="X"
        else:
            fractal+=" "

    for x in range(size):
        print( fractal[x*size:(x*size)+size])

print_board_fractal(board,square_fractal,size)
