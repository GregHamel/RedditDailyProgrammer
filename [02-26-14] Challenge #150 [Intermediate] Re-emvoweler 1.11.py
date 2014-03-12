#[02-26-14] Challenge #150 [Intermediate] Re-emvoweler 1
#http://www.reddit.com/r/dailyprogrammer/comments/1yzlde/022614_challenge_150_intermediate_reemvoweler_1/

import re
import string
import random
import cProfile

#Challenge 149 easy solution--------------
def disemvoweler(s):
    return( re.sub("[aeiou ]","",s), re.sub("[^aeiou]","",s))
#------------------------------------------

input_cons, input_vowels = disemvoweler("bbsrshpdlkftbllsndhvmrbndblbnsthndlts aieaeaeieooaaaeoeeaeoeaau")

print( input_cons, input_vowels )

word_list = [w.strip() for w in open("challenge150Iwords.txt").readlines()]
word_dict = {k:[] for k in [x+y for x in string.ascii_lowercase for y in string.ascii_lowercase]+
            [x+y+z for x in string.ascii_lowercase for y in string.ascii_lowercase for z in string.ascii_lowercase]}
dict_of_word_lists = {}

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
            print ( new_output[:-1] )

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
        reemvoweler(input_cons, input_vowels)

cProfile.run("run_reemvoweler(100000,input_cons,input_vowels)")



