

##[11-12-13] Challenge #135 [Intermediate] De Morgan's Law

f = open("challenge135I.txt")

raw_data = [x.strip() for x in f.readlines()]

def de_Morgan(expression):
    parts = expression.split()
    new_parts = []
    inside_paren = False
    prev = ""
    for p in parts:
        if p[0] == "(":
            inside_paren = True
            if prev != "NOT":
                new_parts.append("NOT")
            new_parts.append(p)
            continue
        if p[-1] == ")":
            prev = ")"
            new_parts.append(p)
            inside_paren = False
            continue
        if inside_paren:
            prev = "("
            new_parts.append(p)
            continue
        if p == "NOT":
            prev = "NOT"
            continue
        if p in "abcdefg":
            if prev is "NOT":
                prev = p
                new_parts.append(p)
                continue
            else:
                prev = p
                new_parts.append("NOT")
                new_parts.append(p)
                continue
        if p == "OR":
            prev = p
            new_parts.append("AND")
            continue
        if p == "AND":
            prev = p
            new_parts.append("OR")

    print(" ".join(new_parts))

de_Morgan(raw_data[0])