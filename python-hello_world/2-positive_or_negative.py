import random
number = random.randint(-10, 10)

if number >0:
    print("\n {} Positive" .format(number))
elif number<0:
    print("\n {} Negative" .format(number))
else:
    print("\n {} Zero" .format(number))
