
c = "thffcrrprtdthtblckdndcrfwhdbnrdrd"
v =  "eoieeoeaaoaeaaueaeeoee"

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

print(find_prefixes(c,v))