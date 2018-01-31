import random

def MontyHall(choice, monty_stall=[1,0,0]):
    count = 1 - monty_stall[choice]
    return count

monty_stall = [1,0,0]
N = 10000

wins = 0.0
for i in range(N):
    real_choice = random.randint(0,2)
    count = MontyHall(real_choice)
    wins = wins + count 

p = wins/N
print('Trys',  N, 'wins ', wins, ' prob of winning', p)

