#[6/14/2014] Challenge #166b [Intermediate] Prime Factor Trees
#http://www.reddit.com/r/dailyprogrammer/comments/284uhh/6142014_challenge_166b_intermediate_prime_factor/
import math

def prime_factorization(n):
    print(n)
    factors = find_factors(n)
    while True:
        f = factors.pop()
        new_f = find_factors(f)
        if new_f == []:
            return factors+[f]
        else:
            factors+=new_f

def find_factors(n):
    factors = []
    for num in range(2, int(math.sqrt(n)//1)+1):
        if n%num==0:
            factors.append(num)
            factors.append(n//num)
            break
    return factors

print(prime_factorization(72))