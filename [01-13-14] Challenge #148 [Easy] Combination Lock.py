#[01-13-14] Challenge #148 [Easy] Combination Lock
#http://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/

lock = [5, 1, 2, 3]
rotation_increments = 3*lock[0]+lock[1]+(lock[1]-lock[2])%lock[0]+(lock[3]-lock[2])%lock[0]

print(rotation_increments)