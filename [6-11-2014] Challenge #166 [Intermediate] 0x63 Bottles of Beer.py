#[6/11/2014] Challenge #166 [Intermediate] 0x63 Bottles of Beer
#http://www.reddit.com/r/dailyprogrammer/comments/27vxj9/6112014_challenge_166_intermediate_0x63_bottles/

fibs_to_calc=[[66, 79, 84, 84, 76, 69, 83, 32, 79, 70, 32, 66, 69, 69, 82],\
        [79, 78, 32, 84, 72, 69, 32, 87, 65, 76, 76],\
        [84, 65, 75, 69, 32, 79, 78, 69, 32, 68, 79, 87, 78, 44, 32, 80, 65,\
        83, 83, 32, 73, 84, 32, 65, 82, 79, 85, 78, 68]]

def fibonnaci(n):
    if n < 2:
        return 1
    else:
        return (fibonnaci(n-(n-1)) + fibonnaci((n-1)-(n-2))*(n-1))

def first_n_fibonnaci(n):
    fibs = []
    for num in range(n):
        fibs.append(fibonnaci(num+1))
    fibs1 = "".join([chr(l) for l in fibs_to_calc[0]])
    fibs2 = "".join([chr(l) for l in fibs_to_calc[1]])
    fibs3 = "".join([chr(l) for l in fibs_to_calc[2]])
    for f in fibs[::-1]:
        print( "{0} {1} {2} {0} {1} {3} {4} {1} {2} ".format(f, fibs1, fibs2, fibs3, f-1))

first_n_fibonnaci(100)
