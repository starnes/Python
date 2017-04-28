import random

class Color:
    pass

c1 = Color()
c2 = Color()
c3 = Color()

guesses_made = 0

c1.name = input('Hello! What is your name?\n')

c2.color = ['blue', 'green', 'red', 'orange', 'purple', 'pink']

c2.color = random.choice(c2.color)
print 'Well, {0}, I am thinking of a color between blue, green, red, orange, purple and pink.'.format(c1.name)

while guesses_made < 3:

    c3.guess = input('Take a guess: ')

    guesses_made += 1

    if c3.guess != c2.color:
        print 'Your guess is wrong.'

    if c3.guess == c2.color:
        break

if c3.guess == c2.color:
    print 'Good job, {0}! You guessed my color in {1} guesses!'.format(c1.name, guesses_made)
else:
    print 'Nope. The color I was thinking of was {0}'.format(c2.color)