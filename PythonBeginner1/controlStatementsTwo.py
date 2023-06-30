#IfElse
#Input a number and print whether number is positive or not
N = int(input())
if N > 0:
    print("Positive")
else:
    print("Not Positive")



#example
#Odd or even
O = int(input())
if O % 2 == 0:
    print("Even")
else:
    print("Odd")



#example
#favourite language
Lang = input()
if Lang == "Python":
    print("Nice Choice!")
else:
    print("I dont know that language")



#example
#F L 2
if Lang == "Python" or Lang == "Java":
    print("Nice Choice!")
else:
    print("I dont know that language")



#elif
#example
#F L 3
if Lang == "Python" or Lang == "Java":
    print("Nice Choice!")
elif Lang == "C++":
    print("I am Speed")
else:
    print("I dont know that language")



#Example
# F L 4
if Lang == "Python" or Lang == "Java":
    print("Nice Choice!")
elif Lang == "C++":
    print("I am Speed")
elif Lang == "Javascript":
    print("Oh. You are a web developer")
elif Lang == "Golang":
    print("You're a cool person, I see")
else:
    print("I dont know the Language")



#example
N = int(input())
if N > 0:
    print("Positive")
elif N == 0:
    print("Zero")
else:
    print("Negative")



#example
a = 1
b = 0
c = 1
if (a and b):
    print("AI is awesome")
elif (a and c):
    print("ML is amazing")
if (a and b and c):
    print("Python is amazing")
if (a or b or c):
    print("I love DS")



#Independent if-else
'''Given an integer, check if it is odd or even and then also check if it is divisible by 3
or not. Then also check if it is divisible by 5.
'''
I = int(input())
if I % 2 == 0:
    print("Even")
else:
    print("Odd")
if I % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")
if I % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


#FizzBuzz
#Important example
'''
Write a program that takes in a number N as input and does the following
- if N is a multiple of only 3, print Fizz
- if N is a multiple of only 5, print Buzz
- if N is a multiple of both 3 and 5, print FizzBuzz
'''
print("FizzBuzz Input")
FB = int(input())
if FB % 5 == 0 and FB % 3 == 0:
    print("FizzBuzz")
elif FB % 5 == 0:
    print("Buzz")
elif FB % 3 == 0:
    print("Fizz")



#example
'''
Write a program that asks the user to input a number N. If N is between 10 and 20, your program should ask the user to enter another number M and then:-

-Print the sum of the two numbers.
-If the sum is greater than equal to 100, your program should also print "That is a large sum!" on a new line.
-If N is not between 10 and 20, your program should print -1.
'''
N = int(input())
if N >= 10 and N <= 20:
    M = int(input())
    print(N + M)
    if N + M >= 100:
        print("That is a large sum!")
else:
    print(-1)



#example
'''
Given an integer A representing an year, Return 1 if it is a leap year else return 0.

A year is leap year if the following conditions are satisfied:

-Year is multiple of 400.
-Else the year is multiple of 4 and not multiple of 100.
'''
L = int(input())
if L % 400:
    print(1)
elif L % 4 and not L % 100:
    print(1)
else:
    print(0)






