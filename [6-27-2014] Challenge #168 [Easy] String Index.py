#[6/27/2014] Challenge #168 [Easy] String Index
#http://www.reddit.com/r/dailyprogrammer/comments/299hvt/6272014_challenge_168_easy_string_index/
import re

str_to_index = "...You...!!!@!3124131212 Hello have this is a --- string \
                 Solved !!...? to test @\n\n\n#!#@#@%$**#$@ Congratz this!!\
                 # !!!!!!!!!!!!!!one ---Problem\n\n"

strings = re.findall("[a-zA-Z0-9]+",str_to_index)
index_list = [12, -1, 1, -100, 4, 1000, 9, -1000, 16, 13, 17, 15]
new_str = ""

for i in index_list:
    if i in range(len(strings)+1):
        new_str+=strings[i-1]
    new_str+=" "
print(new_str)
