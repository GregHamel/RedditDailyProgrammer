#[02-26-14] Challenge #150 [Intermediate] Re-emvoweler 1
#http://www.reddit.com/r/dailyprogrammer/comments/1yzlde/022614_challenge_150_intermediate_reemvoweler_1/
#                        and
#Solution to [02/24/14] Challenge #149 [Easy] Disemvoweler
#http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/

import re
import string
import random
import cProfile

#Challenge 149 easy solution--------------
def disemvoweler(s):
    return( re.sub("[aeiou ]","",s), re.sub("[^aeiou]","",s))
#------------------------------------------

input_cons, input_vowels = disemvoweler("bbsrshpdlkftbllsndhvmrbndblbnsthndlts aieaeaeieooaaaeoeeaeoeaau")


word_list = [w.strip() for w in open("challenge150Iwords.txt").readlines()]
word_dict = {k+l:[] for k in string.ascii_lowercase for l in string.ascii_lowercase}
dict_of_word_lists = {}
list_of_solutions =[]

for word in word_list:
    word_dict[word[0]+word[1]]+=[word]

def reemvoweler(consonant_string, vowel_string, output="", stop_at=1000):
    if len(list_of_solutions) >= stop_at:
        return
    new_word_list = get_valid_words(consonant_string, vowel_string)
    if new_word_list != []:
        for w in new_word_list:
            new_word = w[0]
            new_cons = consonant_string[w[1]:]
            new_vowels = vowel_string[w[2]:]
            new_output = output+new_word+" "
            if (len(new_vowels)+len(new_cons)) > 1:
                reemvoweler(new_cons, new_vowels, output=new_output, stop_at=stop_at)
            elif new_vowels == "" and new_cons == "":
                list_of_solutions.append( new_output[:-1] )

def get_valid_words(consonant_string, vowel_string):
    if  consonant_string+vowel_string in dict_of_word_lists:
        return dict_of_word_lists[consonant_string+vowel_string]
    valid_words, words_to_search = ([], [])
    num_cons, num_vowels = (len(consonant_string), len(vowel_string))

    if num_cons > 1 and num_vowels > 0:
        words_to_search+=word_dict[consonant_string[0]+consonant_string[1]] + word_dict[consonant_string[0]+vowel_string[0]]
    elif num_cons == 1:
        words_to_search+=word_dict[consonant_string[0]+vowel_string[0]]
    elif num_cons > 1:
        words_to_search+=word_dict[consonant_string[0]+consonant_string[1]]
    if num_vowels > 1 and num_cons > 0:
        words_to_search+=word_dict[vowel_string[0]+vowel_string[1]] + word_dict[vowel_string[0]+consonant_string[0]]
    elif num_vowels == 1:
        words_to_search+=word_dict[vowel_string[0]+consonant_string[0]]
    elif num_vowels > 1:
        words_to_search+=word_dict[vowel_string[0]+vowel_string[1]]

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


cProfile.run("reemvoweler(input_cons, input_vowels, stop_at=1000)")

print("Number of Solutions found:", len(list_of_solutions))
for x in range(5):
    if len(list_of_solutions) > x:
        print (list_of_solutions[x], "\n",list_of_solutions[-x-1])

##for word in list_of_solutions:
##    print(word)





