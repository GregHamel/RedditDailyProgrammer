

## [11/4/13] Challenge #140 [Easy] Variable Notation
#http://www.reddit.com/r/dailyprogrammer/comments/1q6pq5/11413_challenge_140_easy_variable_notation/

f = open("challenge140.txt")

raw_data = [x.strip() for x in f.readlines()]
data = [x for x in zip(raw_data[0::3], raw_data[1::3])]

def translate_variables(data):
    for var in data:
        print(var[0])
        if var[0] == "0":
            words = [var[1].split()[0]]+[x.capitalize() for x in var[1].split()[1:]]
            print("".join(words))
        if var[0] == "1":
            words = var[1].split()
            print("_".join(words))
        else:
            words = [x.upper() for x in var[1].split()]
            print("_".join(words))

translate_variables(data)