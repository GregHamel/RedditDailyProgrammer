#[5/19/2014] Challenge #163 [Easy] Probability Distribution of a 6 Sided Di
#http://www.reddit.com/r/dailyprogrammer/comments/25y2d0/5192014_challenge_163_easy_probability/
import random

def die_roller(num_rolls):
    rolls={1:0,2:0,3:0,4:0,5:0,6:0}
    for roll in range(num_rolls):
        rolls[random.randint(1,6)]+=1
    return rolls

def roll_tester(num_rolls):
    print("""# of Rolls 1s     2s     3s     4s     5s     6s
          ====================================================""")
    num_rolls_list = [10**x for x in range(1,num_rolls+1)]
    for i,roll in enumerate(num_rolls_list):
        n_rolls = die_roller(roll)
        percentages = ["{0:.2f}%".format((num/roll)*100) for num in n_rolls.values()]
        print(roll, (" "*(num_rolls-i)) , " ".join(percentages))

roll_tester(7)