#[08-13-13] Challenge #135 [Easy] Arithmetic Equations
#http://www.reddit.com/r/dailyprogrammer/comments/1k7s7p/081313_challenge_135_easy_arithmetic_equations/

import random

r = input("Enter range").split()

def arithmetic(range_start, range_stop):
    operations = "*+-"
    nums = [random.randint(range_start, range_stop) for x in range(4)]
    problem = " ".join([str(x) +" "+ random.choice(operations) for x in nums])[:-1]
    user_answer = input(problem)
    real_answer = str(eval(problem))
    if user_answer == "Q" or user_answer == "q":
        print ("Thanks for playing!")
    elif user_answer == real_answer:
        print ("Correct! The answer was " + real_answer)
        arithmetic(range_start, range_stop)
    else:
        print ("Incorrect! The answer was " + real_answer)
        arithmetic(range_start, range_stop)

arithmetic(int(r[0]),int(r[1]))
