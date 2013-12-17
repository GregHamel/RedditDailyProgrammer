
#[08/06/13] Challenge #134 [Easy] N-Divisible Digits
#http://www.reddit.com/r/dailyprogrammer/comments/1jtryq/080613_challenge_134_easy_ndivisible_digits/

import time

def n_digits(N,M):
    for x in range(int("9"*N),0,-1):
        if x%M == 0 and len(str(x)) == N:
            return x
    return None

start = time.clock()

def n_digits(N,M):
    return int("9"*N) - (int("9"*N) %M)

print (n_digits(9,641351511))


stop = time.clock()
print(stop-start)

