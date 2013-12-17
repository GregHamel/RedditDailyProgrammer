
#[11/4/13] Challenge #139 [Easy] Pangrams
#http://www.reddit.com/r/dailyprogrammer/comments/1pwl73/11413_challenge_139_easy_pangrams/

import string


f = open("Challenge139.txt")

num_lines = int(f.readline())
lines = [x.strip() for x in f.readlines()]

letters = string.ascii_lowercase

def find_pangrams(lines):
    for line in lines:
        appearances = {k:v for (k,v) in zip(letters,[0 for l in letters])}

        for letter in line.lower():
            if letter in appearances:
                appearances[letter]+=1

        pangram = True
        for letter in appearances:
            if appearances[letter] == 0:
                pangram = False
                break

        print(pangram)
        print(appearances)


find_pangrams(lines)