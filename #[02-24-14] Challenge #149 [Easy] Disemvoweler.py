#[02-24-14] Challenge #149 [Easy] Disemvoweler
#http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/


import re

def disemvoweler(s):
    print( re.sub("[aeiou ]","",s))
    print( re.sub("[^aeiou]","",s))