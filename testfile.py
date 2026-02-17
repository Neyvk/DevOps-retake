import random
number = random.randint(1, 100)
attempts = 0  # count no of attempts to guess the number
guess = 0
while guess != number:
    guess = eval(raw_input('Guess a number: '))
    attempts += 1
    if guess == number:
        print('Correct! You used', attempts, 'attempts!')
        break
    elif guess < number:
        print ('Go higher!')
    else:
        print("Go lower!")

def roll_dice_and_compute_sum(ndice):
    return sum([random.randint(1, 6) for i in range(ndice)])
                

def computer_guess(ndice):
    return random.randint(ndice, 6*ndice)

def player_guess(ndice):
    return input('Guess the sum of the no of eyes in the next throw: ')

def play_one_round(ndice, capital, guess_function):
    guess = guess_function(ndice)
    throw = roll_dice_and_compute_sum(ndice)
    if guess == throw:
        capital += guess
    else:
        capital -= 1
    return capital, throw, guess