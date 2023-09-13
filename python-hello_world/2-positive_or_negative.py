import random
number = random.randint(-10, 10)

if number >0:
    print("\n {} is Positive" .format(number))
elif number==0:
   print("\n {} is Zero" .format(number))
else:
   print("\n {} is Negative" .format(number))
