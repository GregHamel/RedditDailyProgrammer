import re

def disemvoweler(s):
    print( re.sub("[aeiou ]","",s))
    print( re.sub("[^aeiou]","",s))