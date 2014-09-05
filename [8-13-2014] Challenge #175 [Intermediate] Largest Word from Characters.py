#[8/13/2014] Challenge #175 [Intermediate] Largest Word from Characters
#http://www.reddit.com/r/dailyprogrammer/comments/2dgd5v/8132014_challenge_175_intermediate_largest_word/

input1 = "hello yyyyyyy yzyzyzyzyzyz mellow well yo kellow lellow abcdefhijkl hi is yellow just here to add strings fellow lellow llleow"
input2 = "l e l o h m f y z a b w"

def find_words(str1, str2):
    words = str1.split()
    letters = str2.split()
    longest = 0
    longest_list = []

    for word in words:
        if len(word) > len(letters) or len(word)< longest:
            continue
        sortword = sorted(word)
        sortletters = sorted(letters)
        works = True
        for letter in sortword:
            if letter not in sortletters:
                works = False
                break
            else:
                sortletters.remove(letter)
        if works:
            if len(word) > longest:
                longest = len(word)
                longest_list = [word]
            else:
                longest_list.append(word)

    return longest_list

print ( find_words(input1, input2) )
