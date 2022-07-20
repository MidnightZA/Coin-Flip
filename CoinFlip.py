import random

# Ask user how many tosses they will like to test
def numberOfTosses():
    tosses = 0
    while tosses < 1:
        try:
            tosses = int(input('How many tosses would you like to perform?: '))
        except ValueError:
            print('Not a Number, try again')
        else:
            if tosses < 0:
                print('Tries cannot be NEGATIVE!!')
            elif tosses == 0:
                print('Tries cannot be ZERO')

    return tosses


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

#
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
