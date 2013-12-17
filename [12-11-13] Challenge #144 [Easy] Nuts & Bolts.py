
##[12-11-13] Challenge #144 [Easy] Nuts & Bolts
##http://www.reddit.com/r/dailyprogrammer/comments/1sob1e/121113_challenge_144_easy_nuts_bolts/

data = [x.strip() for x in open("challenge144.txt").readlines()]

old_prices = sorted(data[1:int(data[0])+1])
new_prices = sorted(data[int(data[0])+1:])
diff_prices =[(x.split(),y.split()) for x,y in zip(old_prices,new_prices) if x not in new_prices]

for d in diff_prices:
    diff = int(d[1][1])-int(d[0][1])
    print ("{} {:+}".format(d[0][0], diff))

