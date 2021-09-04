# A student has taken 3 tests in a class, and wants to know their current grade 
# (which is only calculated by these tests). 

# Ask the user to input all three of the test scores for the student, one by one. 

# The program should then calculate the average test score (average is adding all three 
# test scores together then dividing by 3), and then print the student's letter grade 
# (as well as the average score as a number).


test1 = int(input("Input first test score: "))
test2 = int(input("Input second test score: "))
test3 = int(input("Input third test score: "))
avg = int((test1+test2+test3)/3)
print(avg)
avg1 = avg/100
if avg1 >=.90:
    print("A")
elif avg1 >=.80:
    print("B")
elif avg1 >= .70:
    print("C")
elif avg1 >= .6:
    print("D")
else:
    print("F")

import math
# Gregory wants to know how many toys they can buy at Toys'N'Us

# They prioritize buying the most expensive toys first (For ejm. If Gregory had $50 
# they'd end up buying 2 Jumbo Baby Yoda Plushies, 1 Beyblade, and 5 Sticky Hands with 
# a remainder of $0.30 left)

# Have the user input how much money Gregory has then print how many of each 
# toy they can afford, as well as how much money they'd have remaining

#Jumbo Baby yoda plush - $20
#beyblae - $7.2
#stickt hand - $.5
money = int(input("How much money does Greg have? "))
jumbo = money % 20
jumbo1= money//20
print("Gregory can afford", jumbo1, "Jumbo Baby yoda plushies.")
beyblae = jumbo % 7.2
beyblae1 = (jumbo) // 7.2
print("Gregory can afford", beyblae1, "beyblades.")
sthand = int(beyblae // .5)
remainder = money - (jumbo1*20) - (beyblae1*7.2) - (sthand*.5)

print("Gregory can afford", sthand, "sticky hands")
print("Remainder of", math.ceil(remainder*10)/10, "dollars left.")