#[4-24-2014] Challenge #154 [Easy] March Madness Brackets
#http://www.reddit.com/r/dailyprogrammer/comments/217klv/4242014_challenge_154_easy_march_madness_brackets/

import re
example = "{years [four score] ago (and seven) our fathers}"

levels = sum([1 for x in example if x in "{[("])
levels_dict = {k:"" for k in range(1,levels+1)}
current_lev = 0
for letter in example:
    if letter in("{[("):
        current_lev+=1
    elif letter in("]})"):
        levels_dict[current_lev] += " "
        current_lev-=1
    else:
        levels_dict[current_lev] += letter

print( " ".join([re.sub(" +"," ",levels_dict[lev].strip()) for lev in range(levels,0,-1)]) )



