#python3
import random
number = random.randint(-10000, 10000)
last_digit = number%10
#code is here
if last_digit >5:
    print("\n The last number {} is {} and is greater than 5" .format(number, last_digit))
elif last_digit ==0:
    print("\n The last number {} is {} and is 0" .format(number, last_digit))
else:
    print("\n The last number {} is {} and is less than 6 and not 0" .format(number, last_digit))
