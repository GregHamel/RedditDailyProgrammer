#[5-5-2014] #161 [Easy] Blackjack!
#http://www.reddit.com/r/dailyprogrammer/comments/24r50l/552014_161_easy_blackjack/
import random

DECK = [(x,y) for x in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] for y in ("D","S","C","H")]
VALUES = {k:v for k,v in zip([2,3,4,5,6,7,8,9,10,"J","Q","K","A"],[2,3,4,5,6,7,8,9,10,10,10,10,11])}

def deal_hands(number_of_hands, number_of_decks):
    decks = []
    for x in range (number_of_decks):
        decks+= DECK[:]
    random.shuffle(decks)
    hands = []
    card_frequencies= {k:v for k,v in zip([2,3,4,5,6,7,8,9,10,"J","Q","K","A"],[0]*13)}
    blackjacks = 0

    for hand in range(number_of_hands):
        cards = [decks.pop(),decks.pop()]
        value =  0
        aces = 0
        for card in cards:
                if card[0] == "A":
                    aces+=1

        for card in cards:
            value+= VALUES[card[0]]

        while True:
            if value == 21:
                blackjacks+=1
                hands.append([cards,"Blackjack",value])
                for card in cards:
                    card_frequencies[card[0]]+=1
                break
            if value<21:
                hit = decks.pop()
                value+= VALUES[hit[0]]
                cards.append(hit)
                if hit[0] == "A":
                    aces+=1
                continue
            if aces > 0:
                value-=10
                aces-=1
            if value>21:
                hands.append([cards,"Bust",value])
                break

    return (blackjacks, blackjacks/number_of_hands, card_frequencies)


print ( deal_hands(10000, 1000) )