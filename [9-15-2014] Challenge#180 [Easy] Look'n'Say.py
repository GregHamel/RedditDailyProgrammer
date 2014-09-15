#[9/15/2014] Challenge#180 [Easy] Look'n'Say
#http://www.reddit.com/r/dailyprogrammer/comments/2ggy30/9152014_challenge180_easy_looknsay/
import cProfile

def look_say(num):
    str_num = str(num)
    current = ""
    current_count = 0
    final_str = ""
    for x in str_num:
        if current_count == 0:
            current+=x
        if x == current:
            current_count += 1
            continue
        final_str += str(current_count) + current
        current = x
        current_count = 1
    final_str += str(current_count) + current
    return final_str

def n_looks(n,num):
    if n == 1:
        return look_say(num)
    return n_looks(n-1,look_say(num))


