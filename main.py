#test 
from random import randint
correct = randint(1,100) # get a random number
number = None
while number != correct


    print("guess my number")
    number = int(input())
    if number > correct:
        print("LOWER!")
    if number < correct:
        print("HIGHER!")  
    if number == correct:
        print("YOU WON!!!!")

    five_less = correct - 5
    five_more = correct + 5

    if number >= five_less and number <= five_more:
        print("ALMOST! WITHIN 5 AWAY")

