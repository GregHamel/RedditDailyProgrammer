

##[06-17-13] Challenge #132 [Easy] Greatest Common Divisor
#http://www.reddit.com/r/dailyprogrammer/comments/1hvh6u/070813_challenge_132_easy_greatest_common_divisor/

import math

def GCD(num1, num2):
    for x in divisors(num1)[::-1]:
        if x in divisors(num2):
            return x

def divisors(num):
    bottom = [x for x in range(1,int(math.sqrt(num)+1)) if num % x == 0]
    return bottom + [int(num/x) for x in bottom[0:-1]][::-1]

