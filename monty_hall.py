import random

N = int(raw_input("No of simulations = "))
monty_stall = ["cash", "goat", "goat"]
wins = 0.0
losses = 0.0

for i in range(N):
    choice = random.randint(0,2)
    real_choice = monty_stall[choice]
    if (choice == 0):
        wins = wins + 1
    elif (choice == 1):
        wins = wins + 1
    elif (choice == 2):
        losses = losses + 1

P = (wins/N)

print "Total no of win :",wins
print "The probability of winning the cash =",P
