#Assignment Operator
x = 3
y = 4
x = x + 5
y = y - 5
print(x) #Prints 8
print(y) #prints -1

#Compound Assignment
x = 10
y = 5
y -= 10     # nothing but y = y - 10
print(y)
x += 5      # nothing but x = x + 5
print(x)
x *= 3      # nothing but x = x * 3
print(x)
y /= 6      # nothing but y = y / 6
print(y)
x //= 6     # nothing but x = x // 6
print(x)
y %= 7      # nothing but y = y % 7
print(y)
x **= 4     # nothing but x = x ** 4
print(x)


#Logical Operators
#and, or, not
print(25 > 50 or 1 != 2) # prints True
print(10 > 5 and 20 < 100) # prints True
print(10 > 5 and 20 < 6) #prints False

#example
#given age and citizenship of a person, check if they are eligible to vote in India.
age = 20
citizenship = "American"

print(age <= 18 and citizenship == "Indian") #prints False



#Branching - if-else
#example
temp = int(input())
if temp > 20:
    print("Wear a T Shirt")
else:
    print("Wear a Jacket")



#example
#Password Validation System
'''
password matchs -> match
passwords do not match -> Try again
'''
Pass = input()
Confirm_Pass = input()
if Pass == Confirm_Pass:
    print('Match')
else:
    print("Try Again")



#example
'''
Check if the number is positive, if positive write input number is positive.
'''
number = int(input())
if number > 0:
    print("Input number is positive")


#example
'''
Let us say you are recording the score for course. The maximum score is 100, 50 for theoretical work and
50 for practical. You want to display an error message if the total is more than 100.
'''
mark_theoretical = int(input())
mark_practical = int(input())
if mark_theoretical <= 50 and mark_practical <= 50:
    print('OK')
else:
    print("Something is wrong")


#example
#what is the max of 2 numbers
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)


#example not operator
person = "sam"

if not (person == "ram"):
    print("Hello")
else:
    print("Hi")


#example
'''You have been given a dataset for marks of 2 subjects, scored by students of 
classes ClassA and ClassB. You now want to compare the performances of class A 
and class B by finding out the average performance of the classes. Write a program 
to find if class A performed better. Print True is Class A is strictly better else 
return False.
'''
ClassA_SubA = int(input())
ClassA_SubB = int(input())
ClassB_SubA = int(input())
ClassB_SubB = int(input())
Avg_ClassA = (ClassA_SubA + ClassA_SubB) / 2
Avg_ClassB = (ClassB_SubA + ClassB_SubB) / 2
if Avg_ClassA > Avg_ClassB:
    print(True)
else:
    print(False)



