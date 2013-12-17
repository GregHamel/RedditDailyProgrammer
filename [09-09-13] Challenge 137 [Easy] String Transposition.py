

#[08/13/13] Challenge #137 [Easy] String Transposition
#http://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/


f = [s.strip() for s in open("challenge137.txt").readlines()]
max_len = max([len(s) for s in f])
padded = [s+" "*((max_len)-len(s)) for s in f]

for c in range(max_len):
    seg = ""
    for s in padded:
        seg +=(s[c])
    print (seg)

