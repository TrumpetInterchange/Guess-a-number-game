import functions
guess_count = 0
print(
    '===G U E S S - T H E - N U M B E R===' #Game start up
)

while guess_count < 15 or guess_count == 15: #They have to get it right in 15 tries
    response = input('Guess a number from 1 to 500\n') #They guess
    if functions.inputCheck(response) !=0:
        #inputCheck() returns 0 when it's not valid. Therefore this runs when it's valid
        guess_count = guess_count+1
        if functions.rangeCheck(functions.inputCheck(response)) == 0: #When it's greater than the answer
            print(f'Too big. Lower. You have {15-guess_count} tries left')
        elif functions.rangeCheck(functions.inputCheck(response)) == 1: #When it's too small
            print(f'Too Small. Higher. You have {15-guess_count} tries left')
        elif functions.rangeCheck(functions.inputCheck(response)) == 2: #When they get it right
            print(f'Congratulations! You got it right in {guess_count} tries!')
            break
    else:
        print('Not a valid guess. Guess a number from 1 to 500') #When the response type is not correct or is out of the range(1,500)
    if guess_count > 15:
        print(f'Game over. Your answer was {functions.ANSWER}.') #When they run out of tries
        break