arr = [10, 12, 8, 2, 9, 3, 4]
target = 3

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1    
    
print(linearSearch(arr, target))
