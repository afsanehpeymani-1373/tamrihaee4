# tamrin 4-1 - ravesh aval
import random

random_number = random.randint(0, 10)
print(random_number)
guess_number = int(input("please enter guess number: "))
guess_try = 1
while random_number != guess_number and guess_try != 4:
    if random_number <= guess_number:
        print(" meghar bishtar ast")
    elif random_number >= guess_number:
        print(" meghar kamtar ast")
    guess_number = int(input("please again enter guess number: "))
    guess_try += 1
else:
    if guess_number != random_number:
        print(" tedad harekat shoma tamam shod")
    else:
        print(" afarin dorost hada zadin")

#-------------------------------------------------
# tamrin 4-1 - ravesh dovom
import random

random_number = random.randint(0, 10)
print(random_number)
guess_number = int(input("please enter guess number: "))
guess_try = 1
while random_number != guess_number:
    if random_number <= guess_number:
        print(" meghar bishtar ast")
    else:
        print(" meghar kamtar ast")
    guess_number = int(input("please enter guess number again: "))
    guess_try += 1
    if guess_try == 4: # barnameh bad az
        quit()
print(" afarin dorost hada zadin")
