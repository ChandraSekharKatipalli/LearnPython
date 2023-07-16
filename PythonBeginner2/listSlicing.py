#MAP Function
a = [5, 9, 1, 4, 3]

def square(x):
    return(x * x)

b = map(square, a)
#convert this map object to list
b = list(map(square, a))
print(b)

#Mapping a input list
s = input()
l = s.split(' ')

def strToInt(x):
    return(int(x))

l = list(map(strToInt, l))
print(l)

#simplify
l = list(map(int, input().split()))
print(l)


#LIST SLICING
runs = [100, 89, 0, 70, 23, 56, 121, 43, 58, 90]

odd_runs = runs[1: len(runs)+1: 2]
print(odd_runs)
even_runs = runs[0: len(runs)+1: 2]
print(even_runs)
first_5 = runs[0 : 5]
print(first_5)
last_5 = runs[-1 : -5: -1]
print(last_5)

a = [10, 20, 30, 40, 50]
print(a[3::-1])
print(a[3:])
print(a[:])
print(a[:2:-1])
print(a[:0:-2])


#REVERSE of a LIST
a = [10, 20, 30, 40, 50, 60]

b = a[-1::-1]
c = a[::-1]
print(b)
print(c)

#REVERSE of a String
hello  = 'Hello world'
print(hello[::-1])


#Rotated Array
#Rotate the array by 1 time
#Pick the first element and put it at the last
#[7, 0, 6, 1, 3]
#[0, 6, 1, 3, 7]
a = [7, 0, 6, 1, 3]

#Array after 3 rotations
def threeRotations(a):
    return a[3:] + a[:3]

def twoRotations(a):
    return a[2:] + a[:2]

print(threeRotations([5,6,7,8,9,0]))
print(twoRotations([5,6,7,8,9,0]))
print(a[5:] + a[:5])
print(len(a))

#Rotate k times
k = int(input())
s = [10, 20, 30, 40, 50, 60]

if k % len(s) == 0:
    print(s[::-1])
else:
    k %= len(s)
    print(s[k:] + s[:k])