

#[07-15-13] Challenge #133 [Easy] Foot-Traffic Analysis
#http://www.reddit.com/r/dailyprogrammer/comments/1iambu/071513_challenge_133_easy_foottraffic_analysis/


## Foot-Traffic Analysis
"""
Sample Input 1
4
0 0 I 540
1 0 I 540
0 0 O 560
1 0 O 560

Sample Output 1
Room 0, 20 minute average visit, 2 visitor(s) total
"""

def traffic_analysis(text):

    f = open(text)

    events = int(f.readline())
    log = [f.readline().strip().split() for x in range(events)]

    f.close()

    roomdata = {} ## room number: [total visit time, total visitors]

    for entry in range(events):
        person = log[entry][0]
        if log[entry][2] == "O":
            continue
        if log[entry][1] not in roomdata:
            roomdata[log[entry][1]] = [0,1]
        else:
            roomdata[log[entry][1]][1] += 1
        for entry2 in range(events):
            if log[entry2][0] == person and log[entry2][2] == "O" and log[entry2][1] == log[entry][1]:
                leavetime = log[entry2][3]
        roomdata[log[entry][1]][0] += (int(leavetime)+1 - int(log[entry][3]))

    for room in range(0,100):
        if str(room) in roomdata:
            print ("Room "+str(room)+", "+str(roomdata[str(room)][0]//roomdata[str(room)][1])+" minute average visit, "+str(roomdata[str(room)][1])+ " visitor(s) total")


traffic_analysis("sample.txt")

