#SEARCHING
#Linear Search
#Given an array of numbers and a target value, the index of the target value. 
#Return -1 if it is not present in the array
arr = [10, 12, 8, 2, 9, 3, 4]
target = 3

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linearSearch(arr, target))



#Binary Search
#Works for only Sorted arrays
arr = [4, 5, 9, 12, 16, 19, 20, 25]

def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return -1        
    
print(binarySearch(arr, 20))

# for debugging
def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end)//2
        print(f"start = {start}, end = {end}, mid = {mid}")
        print(f"search space = {arr[start:end+1]}")
        print("---------------------------------------------------------------------------------------")
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return -1 

print(binarySearch(arr, 25))



#Square Root
#Given a perfect square number, find its square root.
#(Do not use any inbuilt functions)
#using Binary Search
def perfectSquare(n):
    start = 1
    end = n

    while start <= end:
        mid = (start + end)//2

        if mid ** 2 == n:
            return mid
        elif mid ** 2 < n:
            start = mid + 1
        else:
            end = mid -1
    return (f"{n} is not a perfect square")

print(perfectSquare(100))



#Binary Search takes log(N) steps
#in the worst case scenario