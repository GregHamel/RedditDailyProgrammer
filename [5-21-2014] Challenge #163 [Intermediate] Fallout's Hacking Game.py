#[5/21/2014] Challenge #163 [Intermediate] Fallout's Hacking Game
#http://www.reddit.com/r/dailyprogrammer/comments/263dp1/5212014_challenge_163_intermediate_fallouts/
import random

words = [word.strip() for word in open("challenge163Iwords.txt").readlines()]
difficulty_map= {1:4, 2:5, 3:7, 4:10, 5:15}

def hack_game():
    difficulty = int(input("Select a difficulty level. Type a number 1-5"))
    possibilities = [word for word in words if len(word) == difficulty_map[difficulty]]
    random.shuffle(possibilities)
    selection = possibilities[0:10]
    answer = random.choice(selection)
    guesses = 0
    for word in selection:
        print(word)

    while guesses <4:
        print("{} guesses left.".format(4-guesses))
        guess = input("Enter your guess.")
        if guess == answer:
            print("Correct. You Win!")
            return
        else:
            matches=0
            for i,letter in enumerate(answer):
                for j,letter2 in enumerate(guess):
                    if i==j and letter==letter2:
                        matches+=1
            print("{}/{} correct".format(matches,difficulty_map[difficulty]))
            guesses+=1
    print("Out of guesses. You lose!")

hack_game()
