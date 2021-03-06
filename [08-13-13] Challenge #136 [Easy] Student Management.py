
#[08-13-13] Challenge #136 [Easy] Student Management
#http://www.reddit.com/r/dailyprogrammer/comments/1kphtf/081313_challenge_136_easy_student_management/

sample = """10 10
ABIGAIL 11 3 5 20 4 2 8 17 4 5
ALEXANDER 2 12 20 0 6 10 3 4 9 7
AVA 11 15 2 19 14 5 16 18 15 19
ETHAN 6 12 0 0 5 11 0 11 12 15
ISABELLA 16 0 10 7 20 20 7 2 0 1
JACOB 2 14 17 7 1 11 16 14 14 7
JAYDEN 10 10 3 16 15 16 8 17 15 3
MADISON 10 11 19 4 12 15 7 4 18 13
SOPHIA 5 17 14 7 1 17 18 8 1 2
WILLIAM 12 12 19 9 4 3 0 4 13 14
"""

N, M= int(sample[0:2]), int(sample[3:5])
students = [[s for s in sample[6:].split()][m] for m in range(0,N*M+N,M+1) ]
scores = [int(score) for score in sample[6:].split() if score not in students]

print(sum(scores)/len(scores))
for student in enumerate(students):
    print (student[1], sum(scores[student[0]*M:student[0]*M+M])/M)

