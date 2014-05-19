#[4-11-2014] Challenge #157 [Hard] ASCII Bird
#http://www.reddit.com/r/dailyprogrammer/comments/22slvn/4112014_challenge_157_hard_ascii_bird/
import random
starting_board = [line.strip() for line in open("challenge157H.txt").readlines()]

current_board = []
for line in starting_board:
    b = []
    for letter in line:
        b.append(letter)
    current_board.append(b)

bird_position = [bird for bird, line in enumerate(starting_board) for v in (line) if v[0]=="@"][0]

top_count = [i for i,v in enumerate(current_board[0][::-1]) if v=="#"][0]
bottom_count = [i for i,v in enumerate(current_board[-1][::-1]) if v=="#"][0]
next_top = random.choice(range(7,11))
next_bottom = random.choice(range(7,11))
score = 0

new_lines = ["..........","##........","###.......","####......",\
"##......##","###....###","####..####"]

def print_board(b):
    for line in b:
        print("".join(line))
    print("------------------------------------------")

def advance_board():
    global current_board, score
    nextline1 = get_next_line()
    nextline2 = get_next_line()
    new_board = [line[2:]+[nextline1[i]]+[nextline2[i]] for i,line in enumerate(current_board)]
    new_board[bird_position][1]="@"
    passed1 = [line[2] for i,line in enumerate(current_board)]
    passed2 = [line[3] for i,line in enumerate(current_board)]
    if "#" in "".join(passed1):
        score+=1
    if "#" in "".join(passed2):
        score+=1
    current_board = new_board


def get_next_line():
    global top_count, bottom_count,next_top,next_bottom
    top_count+=1
    bottom_count+=1
    if top_count == next_top and bottom_count == next_bottom:
        newline = random.choice(new_lines[4:])
        next_top = random.choice(range(7,11))
        next_bottom = random.choice(range(7,11))
        top_count = 0
        bottom_count = 0
    elif top_count == next_top:
        newline = random.choice(new_lines[1:4])
        next_top = random.choice(range(7,11))
        top_count = 0
    elif bottom_count == next_bottom:
        newline = random.choice(new_lines[1:4])[::-1]
        next_bottom = random.choice(range(7,11))
        bottom_count = 0
    else:
        newline = new_lines[0]
    return newline

def play_flappy():
    global bird_position
    while True:
        print_board(current_board)
        print("Score:", score)
        move = int(input("Enter a number 0-4"))
        if move > 0:
            bird_position-= move
            if current_board[bird_position+(move//2)][2] =="#":
                print("You ran into a wall!")
                break
        else:
            bird_position+= 2
            if current_board[bird_position-(1)][2] =="#":
                print("You ran into a wall!")
                break
        if bird_position < 0 or bird_position > 9:
            print("You fell off the map! Game Over!")
            break
        if current_board[bird_position][3] == "#":
            print("You ran into a wall!")
            break
        advance_board()

play_flappy()

