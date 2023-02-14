#sufiyah sajan
#functions
#part 6

import myfunctions as my
import random

no_prob = int(input("How many problems would you like to attempt? "))
print()
while no_prob <= 0:
    print("Invalid number, try again")
    no_prob = int(input("How many problems would you like to attempt? "))
    print()
width = int(input("How wide do you want your digits to be? 5-10: "))
print()
while width < 5:
    print("Invalid width, try again")
    width = int(input("How wide do you want your digits to be? 5-10: "))
    print()
while width > 10:
    print("Invalid width, try again")
    width = int(input("How wide do you want your digits to be? 5-10: "))
    print()

counter = 0

for i in range(no_prob):
    print()
    print("Here we go!")
    print()
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    if num1 == 0:
        my.number_0(width)
    elif num1 == 1:
        my.number_1(width)
    elif num1 == 2:
        my.number_2(width)
    elif num1 == 3:
        my.number_3(width)
    elif num1 == 4:
        my.number_4(width)
    elif num1 == 5:
        my.number_5(width)
    elif num1 == 6:
        my.number_6(width)
    elif num1 == 7:
        my.number_7(width)
    elif num1 == 8:
        my.number_8(width)
    elif num1 == 9:
        my.number_9(width)
    print()
    op = random.randint(0,1)
    if op == 0:
        my.plus(width)
    else:
        my.minus(width)
    print()
    if num2 == 0:
        my.number_0(width)
    elif num2 == 1:
        my.number_1(width)
    elif num2 == 2:
        my.number_2(width)
    elif num2 == 3:
        my.number_3(width)
    elif num2 == 4:
        my.number_4(width)
    elif num2 == 5:
        my.number_5(width)
    elif num2 == 6:
        my.number_6(width)
    elif num2 == 7:
        my.number_7(width)
    elif num2 == 8:
        my.number_8(width)
    elif num2 == 9:
        my.number_9(width)
    print()
    useranswer = int(input("= "))
    if op == 0:
        ans = num1 + num2
        if my.check_answer(num1, num2, ans, '+') == True:
            if ans == useranswer:
                print("Correct! The answer is: ", ans)
                counter += 1
            else:
                print("Sorry, that's not correct. The answer was: ", ans)
    else:
        ans = num1 - num2
        if my.check_answer(num1, num2, ans, '-') == True:
            if ans == useranswer:
                print("Correct! The answer is: ", ans)
                counter += 1
            else:
                print("Sorry, that's not correct. The answer was: ", ans)

print()
print("You got ", counter, " out of ", no_prob, " correct!")
