# Ask user how many tosses they would like to test
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
