import random
from numberOfTosses import *


def Counter(tosses):
    tossCount = 0
    headsCount = 0
    tailsCount = 0

    while tossCount < tosses:

        choices = ['heads', 'tails']
        toss = random.choice(choices)

        if toss == 'heads':
            headsCount += 1
        else:
            tailsCount += 1

        tossCount += 1
    return headsCount, tailsCount

tosses = numberOfTosses()
print(f"We will flip a coin {tosses} times\n")

flips = Counter(tosses)

heads = flips[0]
tails = flips[1]

print(f"Number of times it landed on Heads: {heads}")
print(f"Number of times it landed on Tails: {tails}")

pct = heads/tosses * 100
if heads > tails:
    print(f"\nPercentage of times it landed on Heads: {pct}")
else:
    print(f"\nPercentage of times it landed on Tails: {100-pct}")
