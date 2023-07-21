#Sorting | Time Complexity

#Understanding time complexity
'''
there are many algorithms like searching, sorting. To find the better algorithms 
between two we use 2 critera;
Time & Space => execuation time & extra space

Time:
Asysmptotic analysis of algorithms
- observing performance of algorithms for very large inputs
- also know as Big O

How to compute Big O?
1. Count the no of iterations (approx)
2. Get rid of small terms
3. Get rid of constant co efficient


we can compare two equations with tool - DESMOS(using Graph)
'''

#TLE
#Time Limit Exceeded
#10**8 iterations per second - global standard
#any code will get only 1 sec of execution time

#Example - Constraints
'''
Input Size
1 <= N <= 10**10
Linear Search - O(N) - Big O
worst case - 10**10 iterations

Binary Search - O(log2 N)
worst case - log2 10**10 iterations = 34 iterations

Linear search would have given TLE
Binary Search is a better method
'''




#Bubble Sorting
'''
Bubble sort works on the repeatedly swapping of adjacent elements until they are not in the
intended order. it is called bubble sort because the movement of array elements is just like 
the movement of air bubbles in the water. Bubbles in water rise up to the surface; similarly,
the array elements in bubble sort move to the end in each iteration
'''
l = [4, 2, 5, 6, 1, 3]

def bubbleSort(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort(l))


