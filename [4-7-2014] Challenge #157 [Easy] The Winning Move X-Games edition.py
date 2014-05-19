#[4-7-2014] Challenge #157 [Easy] The Winning Move X-Games edition
#http://www.reddit.com/r/dailyprogrammer/comments/22fgs1/472014_challenge_157_easy_the_winning_move_xgames/

data = [line.strip() for line in open("challenge157.txt").readlines()]
to_move, size = data[0], len(data[1])

board = [[letter,x,y] for x, line in enumerate(data[1:]) for y,letter in enumerate(line)]
board = [ board[i*size:i*size+size] for i in range(size)]
board_transpose = [column for column in zip(*board)]
possibs = board+board_transpose+[[row[i] for i, row in enumerate(board)]]\
                              +[[row[-i-1] for i, row in enumerate(board_transpose)]]

def check_win():
    for row in possibs:
        count = 0
        position = ""
        blocked = False
        for letter in row:
            if letter[0] == to_move:
                count+=1
            elif letter[0] == "-":
                position = letter
                continue
            else:
                blocked = True
                break
        if count == size-1 and blocked is False:
            board[position[1]][position[2]] = [to_move]
            for row in board:
                print("".join([x[0] for x in row]))
            return
    print("No Winning Move!")

check_win()
