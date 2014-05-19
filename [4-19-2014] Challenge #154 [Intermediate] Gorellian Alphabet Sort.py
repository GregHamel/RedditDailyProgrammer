#[4-19-2014] Challenge #154 [Intermediate] Gorellian Alphabet Sort
#http://www.reddit.com/r/dailyprogrammer/comments/20sjif/4192014_challenge_154_intermediate_gorellian/


data = [x.strip() for x in open("challenge154I.txt").readlines()]
alphabet = data[0].split(" ")[1].upper()
words = data[1:]
new_order = []

def g_alpha_sort(wordslist, i=0):
    for letter in alphabet:
        possibles = []
        for w in wordslist:
            if len(w)-1 == i:
                if letter == w[i].upper():
                    new_order.append(w)
            if len(w)-1 > i:
                if letter == w[i].upper():
                    possibles.append(w)
        if possibles == []:
            continue
        if len(possibles) == 1:
            new_order.append(possibles[0])
        else:
            g_alpha_sort((possibles), i=i+1)

g_alpha_sort(words, i=0)
print(new_order)


