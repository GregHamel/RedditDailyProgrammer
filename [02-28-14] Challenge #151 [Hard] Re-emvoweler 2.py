#[02-28-14] Challenge #151 [Hard] Re-emvoweler 2
#http://www.reddit.com/r/dailyprogrammer/comments/1z6flq/022814_challenge_151_hard_reemvoweler_2/


import re
import string
import random
import cProfile

#Challenge 149 easy solution--------------
def disemvoweler(s):
    return( re.sub("[aeiou ]","",s), re.sub("[^aeiou]","",s))
#Challenge 149 easy solution--------------

#Helper functions-------------------------
def cons_counter(s):
    return len(re.sub("[aeiou ]","",s))

def vowel_counter(s):
    return len(re.sub("[^aeiou]","",s))
#Helper functions-------------------------

#Challenge 150 intermediate----------------
input_cons, input_vowels = disemvoweler("thhmrthpthsthtnsnvnthblmngsndtrckllcnsprtnsrthtthtlftngrtrvlngbckthrtyyrstnsrhsprntsmtndltmtlymtcngvntsvntgnwbfrlydscrbdsclssc euoeaoeeioeeeooiouaaoieoeueaeaeoaeeaeaeiaieaoeueiaeeeauiaeaeaieiiaeoeaieieaaai")

word_list = [w.strip() for w in open("challenge150Iwords.txt").readlines()]
word_dict = {k:[] for k in [x+y for x in string.ascii_lowercase for y in string.ascii_lowercase]+
            [x+y+z for x in string.ascii_lowercase for y in string.ascii_lowercase for z in string.ascii_lowercase]}
dict_of_word_lists = {}
word_dict["a"]=["a"]
current_list_of_solutions = []

for word in word_list:
    if len(word) > 2:
        word_dict[word[0:3]]+=[word]
    else:
        word_dict[word[0:2]]+=[word]

def reemvoweler(consonant_string, vowel_string, output=""):
    new_word_list = get_valid_words(consonant_string, vowel_string)
    if new_word_list != []:
        new_word = random.choice(new_word_list)
        new_cons = consonant_string[new_word[1]:]
        new_vowels = vowel_string[new_word[2]:]
        new_output = output+new_word[0]+" "
        if (len(new_vowels)+len(new_cons)) > 0:
            reemvoweler(new_cons, new_vowels, output=new_output)
        elif new_vowels == "" and new_cons == "":
            current_list_of_solutions.append(new_output[:-1])

def get_valid_words(consonant_string, vowel_string):
    if  consonant_string+vowel_string in dict_of_word_lists:
        return dict_of_word_lists[consonant_string+vowel_string]
    valid_words, words_to_search = ([], [])
    num_cons, num_vowels = (len(consonant_string), len(vowel_string))

    for w in find_prefixes(consonant_string, vowel_string):
        if w in word_dict:
            words_to_search+=(word_dict[w])

    for word in words_to_search:
        cons_count, vowel_count = (0, 0)
        cons_remaining = num_cons
        vowels_remaining = num_vowels

        for letter in word:
            if cons_remaining > 0:
                if letter == consonant_string[cons_count]:
                    cons_count+=1
                    cons_remaining-=1
                    continue
            if vowels_remaining > 0:
                if letter == vowel_string[vowel_count]:
                    vowel_count+=1
                    vowels_remaining-=1
                    continue
            break

        if cons_count+vowel_count == len(word):
                valid_words.append((word,cons_count, vowel_count))

    dict_of_word_lists[consonant_string+vowel_string] = valid_words
    return valid_words

def find_prefixes(c,v):
    c = list(c)
    v = list(v)
    prefixes = []
    for x in range(0,4):
        for y in range(0,4):
            if x+y < 4 and x+y != 0:
                prefixes.append("".join(c[:x]+v[:y]))
                prefixes.append("".join(v[:x]+c[:y]))
    prefixes.append("".join(c[:1]+v[:1]+c[1:2]))
    prefixes.append("".join(v[:1]+c[:1]+v[1:2]))
    return(set(prefixes))

def run_reemvoweler(n, cons, vowels):
    for x in range(n):
        reemvoweler(cons, vowels)
#Challenge 150 intermediate----------------


#Challenge 151 hard------------------------
current_solution = []

def piecer_togetherer(substring_size, substring_variety, number_of_searches, input_string, working_solution):
    global current_list_of_solutions
    current_list_of_solutions = []
    cons, vowels = disemvoweler(input_string)
    total_c = len(cons)
    total_v = len(vowels)
    for x in range(substring_variety):
        for y in range(substring_variety):
            run_reemvoweler(number_of_searches, cons[:substring_size*2-x], vowels[:substring_size-y])
    current_best = 0
    best_word = ""
    best_piece = ""
    for piece in current_list_of_solutions:
        for word in piece.split():
            if len(word) > current_best:
                current_best = len(word)
                best_piece = piece
                best_word = word
    if best_word != "":
        best_fragments = best_piece.split(best_word)
        if "".join(best_fragments [:1]) != "":
            working_solution.append("".join(best_fragments [:1]))
        working_solution.append(best_word)

        new_input = cons[(cons_counter(best_fragments [:1][0])+cons_counter(best_word)):]+\
        vowels[(vowel_counter(best_fragments [:1][0])+vowel_counter(best_word)):]

        piecer_togetherer(substring_size, substring_variety, number_of_searches, new_input, working_solution)

def another_pass(substring_size, substring_variety, number_of_searches):
    for i,v in enumerate(current_solution):
        if len(current_solution[i].split()) > 1:
            subsolution = []
            piecer_togetherer(8, 9, 500, "".join(v), subsolution)
            current_solution[i] = " ".join(subsolution)


def run_and_show(substring_size, substring_variety, number_of_searches, input_string, working_solution):
    piecer_togetherer(substring_size, substring_variety, number_of_searches, input_string, working_solution)
    another_pass(substring_size, substring_variety, number_of_searches)
    print (re.sub(" +", " ", " ".join(current_solution) ) )

#run_and_show(12, 8, 400, input_cons+input_vowels, current_solution)
#Challenge 151 hard------------------------

cProfile.run("run_and_show(8, 8, 200, input_cons+input_vowels, current_solution)")



