import random

def MontyHall(choice, monty_stall=[1,0,0]):
    s = 1 - monty_stall[choice]
    return s

monty_stall = [1,0,0]
N = int(raw_input("No of simulations = "))

wins = 0.0
for i in range(N):
    real_choice = random.randint(0,2)
    count = MontyHall(real_choice)
    wins = wins + count 

p = wins/N
print 'wins =',wins 
print 'prob of winning =',p

