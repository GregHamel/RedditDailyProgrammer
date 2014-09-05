#[7/14/2014] Challenge #171 [Easy] Hex to 8x8 Bitmap
#http://www.reddit.com/r/dailyprogrammer/comments/2ao99p/7142014_challenge_171_easy_hex_to_8x8_bitmap/

input_pics = [line.split() for line in open("challenge171")]

formatted_pics = []
for pic in input_pics:
    p = []
    for line in pic:
       p.append( list((str(bin(int(line, 16))[2:].zfill(8)).replace("0"," ").replace("1","X"))) )
    formatted_pics.append(p)

def print_pic(pic):
    for line in pic:
        print ("".join(line))
    print(" ")

def pic_zoom(pic):
    new_pic = []
    for line in pic:
        new_line = []
        for v in line:
            new_line+=[v,v]
        new_pic+=[new_line,new_line]
    return new_pic

def pic_rotate(pic, direction):
    if direction == "right":
        new_pic = [line for line in zip(*pic[::-1])]
    else:
        new_pic = pic_rotate(pic_rotate(pic_rotate(pic, "right"),"right"),"right")
    return new_pic

def pic_invert(pic):
    new_pic = []
    for line in pic:
        new_line = []
        for v in line:
            if v == "X":
                new_line.append(" ")
            else:
                new_line.append("X")
        new_pic.append(new_line)
    return new_pic

print_pic( formatted_pics[2])
print_pic( pic_rotate(formatted_pics[2],"left") )
print_pic( pic_invert(formatted_pics[2]) )
print_pic( pic_zoom(formatted_pics[2]) )




