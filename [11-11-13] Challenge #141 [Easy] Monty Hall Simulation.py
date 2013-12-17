
## [11/11/13] Challenge #141 [Easy] Monty Hall Simulation

import random

def monty_hall(n):
    Tactic1 = 0
    Tactic2 = 0
    prizes = ["car","goat","goat"]
    for x in range(n):
        random.shuffle(prizes)
        guess = 0
        if prizes[guess] is "car":
            Tactic1+= 1
        else:
            options = prizes[1:]
            options.remove("goat") #reveal and remove a goat prize from the remaining options
            if options[0] == "car": #if the remaining door contains a car...
                Tactic2+= 1  #then switching to it yields a win
    print ("Tactic 1", Tactic1/n)
    print ("Tactic 2", Tactic2/n)

monty_hall(10000)



