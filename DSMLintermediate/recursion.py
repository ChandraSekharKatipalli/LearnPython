#Recursion code
'''
Solving a problem using a smaller instance of the same problem
/ by using sub problem

Three steps to write a recursion code
1. Make an assumption - decide what your function does & trust that it will 
do it

2. Main logic - solve your bigger problem using a subproblem

3. Base case - when your recursion stops
'''

#example
#sum of dirst N natural numbers
def sum(N): #assumption that this function gives answer
    if N == 1: #Base case
        return 1
    
    return sum(N-1) + N #Subproblem - Main ogic

print(sum(6))


#example
#Factorial of N
def factorial(N):
    if N == 0:
        return 1
    
    return factorial(N -1) * N

print(factorial(5))



#example
#Fibonacci Series
#1,1,2,3,5,8,13,21,34,55,89,144,.......
def fibonacci(N):
    if N == 0 or N == 1:
        return 1
    
    return fibonacci(N-1) + fibonacci(N-2)

print(fibonacci(6))



#example
#given a number N, print all numbers from 1 to N in incresing order using recursion
def incPrint(N):
    if N == 0:
        return
    
    incPrint(N-1)
    return print(N)

print(incPrint(7))



#Dec Print
def decPrint(N):
    if N == 0:
        return
    
    print(N)
    incPrint(N-1)

print(incPrint(7))