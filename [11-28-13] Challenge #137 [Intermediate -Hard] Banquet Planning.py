
## [11-28-13] Challenge #137 [Intermediate / Hard] Banquet Planning
#http://www.reddit.com/r/dailyprogrammer/comments/1rnrs2/112813_challenge_137_intermediate_hard_banquet/

f = open("challenge137I.txt")
raw_data = [line.strip("\n") for line in f.readlines()]

num_items, num_rules = [int(x) for x in raw_data[0].split()]
items = [x for x in raw_data[1:num_items+1]]
rules = [x for x in raw_data[num_items+1:]]

order_dict = {k:0 for k in items}

for item in order_dict:        #Marks items with no ordering
    item_parts = item.split("_")
    exist = False
    for rule in rules:
        for item_part in item_parts:
            if item_part in rule:
                exist = True
    if not exist:
        order_dict[item] = "Warning: " + item +" does not have any ordering."

# Finds the next items to serve
def get_next(orders):
    items_left = [i for i in orders if orders[i] == 0]
    if len(items_left) == 1:
        return items_left
    comes_later = [x.split()[1] for x in rules if "*" not in x.split()[1]]
    wild_cards = [x.split()[1].strip("*") for x in rules if "*" in x.split()[1]]
    next_items = []
    for item in items_left:
        next_item = True
        item_parts = item.split("_")
        for rule in comes_later:
            if item == rule:
                next_item = False
        for part in item_parts:
            for wild in wild_cards:
                if part == wild:
                    next_item = False
        if next_item:
            next_items.append(item)

    for i in next_items:
        items_left.remove(i)

    #This seciton removes rules that are no longer needed
    dead_rules = []
    for item in next_items:
        for rule in rules:
            rule_first = rule.split()[0]
            if item == rule_first:
                dead_rules.append(rule)

    for rule in rules:
        if "*" in rule.split()[0]:
            wild = rule.split()[0].strip("*")
            isin = False
            for item in items_left:
                if wild in item:
                    isin = True
            if isin == False:
                dead_rules.append(rule)

    for rule in dead_rules:
        rules.remove(rule)

    return next_items

#Runs get_next until all items are given an ordering and then prints the ordering
def main():
    iters = 1
    while 0 in order_dict.values():
        next_items = get_next(order_dict)
        for i in next_items:
            order_dict[i] = iters
        iters+=1
    for x in range(1,len(items)): #prints food items in order
        print_items = []
        for item in order_dict:
            if x == order_dict[item]:
                print_items.append(item)
        if print_items != []:
            print (x, print_items)
    for k,v in order_dict.items(): #prints warnings
        if type(v) == str:
            print (k, v)

main()
