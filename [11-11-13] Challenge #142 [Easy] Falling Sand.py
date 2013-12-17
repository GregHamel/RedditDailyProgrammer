

##[11-11-13] Challenge #142 [Easy] Falling Sand

f = open("challenge142.txt")
raw_data = [x for x in f.read() if x != "\n"]
size = int(raw_data[0].strip())
data = raw_data[1:]+["_" for x in range (size)]

def print_field(data):
    count = 0
    while size > count:
        print ("".join(data[count*size:count*size+size]))
        count+=1

def sand_fall(data):
    change = None
    while change != False:
        change = None
        for index, item in enumerate(data):
            if item == ".":
                if data[index+size] == " ":
                    data[index+size] = "."
                    data[index] = " "
                    change = True
        if change == None:
            change = False

sand_fall(data)
print_field(data)
