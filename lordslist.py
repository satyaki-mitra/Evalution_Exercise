class LordsList(object):       
    def giveList(self, N, primes):
        if (2 <= N <= 1000000000000000000):
            i = 2
            factors = []
            while (i * i <= N):
                if (N % i):
                    i += 1
                else:
                    N //= i
                    factors.append(i)
            if N > 1:
                factors.append(N)
            final_list = sorted(factors)
            return final_list


m = 210
p = [2,5]
LordsList().giveList(m, p)
    
        
