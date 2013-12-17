

##[11-20-13] Challenge #136 [Intermediate] Ranked Voting System

f = open("challenge136I.txt")
raw_data = [x.strip() for x in f.readlines()]

num_votes, num_candidates = [int(x) for x in raw_data[0].split()]
candidates = raw_data[1].split()
votes = [x.split() for x in raw_data[2:]]

def ranked_results():
    r = 1
    alive = raw_data[1].split()
    while r < num_candidates:
        candidates_dict = {k:v for (k,v) in zip(alive,[0 for x in alive])}
        for v in votes:
            best, current_vote = num_candidates, num_candidates
            for choice, rank in enumerate(v):
                if int(rank) < best:
                    if candidates[choice] in alive:
                        best = int(rank)
                        current_vote = choice
            candidates_dict[candidates[current_vote]] +=1

        for c in candidates_dict:
            candidates_dict[c] = candidates_dict[c]/num_votes

        print("Round " + str(r) + ":", candidates_dict)

        for c in candidates_dict:
            if candidates_dict[c] > 0.5:
                print (c + " is the winner")
                return

        for c in candidates_dict:
            if candidates_dict[c] == (min(candidates_dict.values())):
                alive.remove(c)
                break

        r+=1

ranked_results()


