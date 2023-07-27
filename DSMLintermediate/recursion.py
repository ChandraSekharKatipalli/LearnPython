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


#Recursion2
#Complexity Analysis
'''
1. Count approx no of recursive calls
2. Find out cost of each call
3. 
'''


#Merge two sorted arrays
A = [-3, 10, 14, 18, 28, 31, 35]
B = [-5, 0, 4]
res = []

def mergeSortedArr(A, B):
    res = []
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1

    if i<len(A):
        res += A[i:]

    if j<len(B):
        res += B[j:]
    return(res)

print(mergeSortedArr(A, B))



#Merge Sort
'''
In Merge sort, the given array is divided into roughly two equal sub - arrays.
These sub-arrays are divided over and over again into halves
untill we end up with arrays having only element each. At last,
we merge the sorted pairs of sub-arrays into a final sorted array.
'''
A = [-3, 10, 14, 43, 1, 3, 8, 9]

def mergeSort(arr):
    N = len(arr)//2
    if N == 1:
        return arr

    #1. Divide
    A = arr[:N]
    B = arr[N:]

    #2. Sort these sorts recursively
    A = mergeSort(A)
    B = mergeSort(B)

    #3. Merge two sorted arrays
    res = mergeSortedArr(A, B)

    return res

print(mergeSort(A))

