

## Reddit [06-17-13] Challenge #130 [Easy] Roll the Dies
#http://www.reddit.com/r/dailyprogrammer/comments/1givnn/061713_challenge_130_easy_roll_the_dies/


 import random

 def die_roller(dice):
   number_of_dice = int(dice[:dice.find("d")])
   sides = int(dice[dice.find("d")+1:])
   result = ""
   for die in range(number_of_dice):
     result += str(random.choice([x for x in range (1,sides+1)]))+" "
   return result[:-1]

print (die_roller("5d20"))


##Bonus, Longest Two-Character Sub-String


