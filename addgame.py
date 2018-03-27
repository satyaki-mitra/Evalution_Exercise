import itertools
class AddGame(object):
    
    def minimum(self, S):
        if (len(S) <= 20):
            n = len(S)
            combinations = [list(comb) for i in range(1, n+1) for comb in itertools.combinations(S, i)]
            list1 = []
            for i in combinations:
                comb_sum = 0
                for j in i:
                    comb_sum = comb_sum + j
                list1.append(comb_sum)
            highest = max(list1)
            lowest = min(list1)
            list2 = range(lowest, highest+2)
            difference = list(set(list2) - set(list1))
            x = min(difference)
            return x
        else:
            print "You should give a list of integers of length 20 or less at the place of S. Read the problem carefully."

l = [883, 66392, 3531, 28257, 1, 14131, 57, 1, 25, 88474, 4, 1, 110, 6, 1769, 220, 442, 7064, 7, 13]            
AddGame().minimum(l)
