#[4-04-2014] Challenge #156 [Hard] uʍop ǝpᴉsd∩ ƃuᴉɥʇǝɯos ɹoɟ ʍoN
#http://www.reddit.com/r/dailyprogrammer/comments/226zqp/4042014_challenge_156_hard_u%CA%8Dop_%C7%9Dp%E1%B4%89sd_%C6%83u%E1%B4%89%C9%A5%CA%87%C7%9D%C9%AFos/

import string

message = [line.strip()[::-1] for line in open("challenge156H.txt").readlines()][::-1]

char_map = {k:v for k,v in zip(string.ascii_letters+string.digits+"?!. ",\
                              "ɐqɔpǝɟƃɥᴉɾʞןɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z0ƖᄅƐㄣϛ9ㄥ86¿¡˙ ")}

for line in message:
    newline = ""
    for letter in line:
        newline+= char_map[letter]
    print(newline)

