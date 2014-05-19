#[4-14-2014] Challenge #158 [Easy] The Torn Number
#http://www.reddit.com/r/dailyprogrammer/comments/230m05/4142014_challenge_158_easy_the_torn_number/
def find_primes(n):
    primes = [2,3]
    primes_so_far = [2,3]
    for num in range(3,n+1):
        for p in primes:
            if num % p == 0:
                primes.append(num)
    return primes

print (find_primes(100))