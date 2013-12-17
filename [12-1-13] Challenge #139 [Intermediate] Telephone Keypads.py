
##[12-1-13] Challenge #139 [Intermediate] Telephone Keypads
##http://www.reddit.com/r/dailyprogrammer/comments/1sody4/12113_challenge_139_intermediate_telephone_keypads/

letters = [line.strip().split() for line in open("challenge139I.txt").readlines()][0]
words = [line.strip() for line in open("challenge139Iwords.txt").readlines()]
digit_dict ={k:v for k,v in zip(range(2,10),
            ("abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"))}

prefix = "".join([digit_dict[int(letter[0])][len(letter)-1] for letter in letters])
prefix_matches = [word for word in words if prefix==word[0:len(prefix)]]

for word in prefix_matches:
    print (word)