print('Welcome to my game!')
secret_number = 1
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won the game !')
        break
else:
    print('Sorry! you fail.')
