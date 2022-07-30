import random
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Please enter your guess)')
guess = input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1
    if flips == 900:
        print('900 flips and there has been ' + str(heads) + ' heads.')
    if flips == 100:
        print('100 flips and there has been ' + str(heads) + ' heads.')
    if flips == 500:
        print('Halfway done, and there has been ' + str(heads) + ' heads.')

print()
print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
if heads == int(guess):
    print('Wow! You were spot on!')

check = int(guess) - heads 

if abs(check) <= 5:
    print('You were close!')
else:
    print('Nope. Not even close.')
