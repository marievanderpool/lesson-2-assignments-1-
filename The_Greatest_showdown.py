#2.) The Greatest Showdown

# Objective: Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. 
# The program should then identify and print out the largest number among the three.

number_1= int(input("Enter a number between 1-10: "))
number_2= int(input("Enter another number between 1-10: "))
number_3= int(input("Enter a 3rd number between 1-10: "))


if number_1 >= number_2 and number_1 >= number_3:
    largest = number_1
elif number_2 > number_1 and number_2 >= number_3:
    largest = number_2
else:
    largest = number_3

print('The largest number is: ', largest)

# Task 2: Identify the Smallest also determine the smallest number among the three and print it out.
#  (For bonus points create a continuous if elif else chain that extends from task 1 and will identify
#  both largest and smallest numbers)

number_1= int(input("Enter a number between 1-10: "))
number_2= int(input("Enter another number between 1-10: "))
number_3= int(input("Enter a 3rd number between 1-10: "))


if number_1 >= number_2 and number_1 >= number_3:
    largest = number_1 
elif number_1<= number_2 and number_1 <= number_3:
    smallest = number_1
elif number_2 > number_1 and number_2 >= number_3:
    largest = number_2
elif number_2 < number_1 and number_2 <= number_3:
    smallest = number_2
elif number_3 < number_1 and number_3 <= number_2:
    smallest = number_3
else:
    largest = number_3

print ("The largest number is: " ,largest)
print ("The smallest number is: ", smallest)