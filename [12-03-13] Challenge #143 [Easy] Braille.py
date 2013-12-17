
##[12-03-13] Challenge #143 [Easy] Braille
#http://www.reddit.com/r/dailyprogrammer/comments/1s061q/120313_challenge_143_easy_braille/


f = open("challenge143.txt")
data = [x.split() for x in [line.strip() for line in f.readlines()]]
raw_letters = [data[x][y] for y in range(len(data[0])) for x in range(3)]
formatted_letters = ["".join(raw_letters[x*3:(x*3)+3]) for x in range(len(data[0]))]

braille = ["O.....","O.O...","OO....","OO.O..","O..O..","OOO...","OOOO..","O.OO..",".OO...",
".OOO..","O...O.","O.O.O.", "OO..O.","OO.OO.","O..OO.","OOO.O.","OOOOO.", "O.OOO.",".OO.O.",
".OOOO.","O...OO","O.O.OO",".OOO.O","OO..OO","OO.OOO","O..OOO"]
braille_dict = {k:v for k,v in zip(braille,'abcdefghijklmnopqrstuvwxyz')}

translation = [braille_dict[letter] for letter in formatted_letters]
print ("".join(translation))

