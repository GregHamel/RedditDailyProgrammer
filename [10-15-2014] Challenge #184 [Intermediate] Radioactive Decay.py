#[10/15/2014] Challenge #184 [Intermediate] Radioactive Decay
#http://www.reddit.com/r/dailyprogrammer/comments/2jcgej/10152014_challenge_184_intermediate_radioactive/

import numpy as np

data = [line.strip() for line in open("challenge184I")]
t = int(data[0])
labels = [letter[0] for letter in data[1].split("->")]
nuclei_decay = np.array([float(x.split()[1]) for x in data[2:]])
nuclei_numbers= np.array([x for x in [100]+([0]*(len(data)-3))])

def decay(nuclei_decay,nuclei_numbers,time):
    for second in range(time):
        decay = nuclei_numbers * nuclei_decay
        gain = np.append([0],decay[0:len(nuclei_numbers)-1])
        nuclei_numbers = nuclei_numbers - decay + gain
    return list(nuclei_numbers)

results = decay(nuclei_decay,nuclei_numbers,t)

for i,l in enumerate(labels):
    print ('{}: {:.4n}%'.format(l,results[i]))

