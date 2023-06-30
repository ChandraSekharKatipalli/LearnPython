#Print END
print("hello world")
print("hello India")

print("hello world", end='\n') #default end value (break)
print("hello India")

print("hello world", end=' and ') #prints both print values in single line with and in middle
print("hello India")

#example
print(5, end='hello\n')
print('world')
print('how', end=' are you')


print('')

#loops
#While Loop
count = 0

while count < 5:
    print("Hello World")
    count += 1


#example
num = 1

while num <= 10:
    print(num)
    num += 1


#example
num = int(input())
i = 1
while i <= num:
    print(i, end=' ')
    i += 1


#example 
#print all odd integers from 1 to N
N = int(input())
i = 1

while i <= N:
    print(i, end=' ')
    i += 2


#example
#print all multiples of 4 from 1 to N
N = int(input())
i = 4

while i <= N:
    print(i, end=' ')
    i += 4


#print all powers of 2 of numbers from 1 to N
N = int(input())
i = 2

while i <= N:
    print(i, end=' ')
    i *= 2


#first 10 numbers of squares of 2
i = 1
N = 10
x = 2

while i <= N:
    print(x, end=' ')
    i += 1
    x *= 2



#print perfect squares of first N times from 1
i = 1
N = 10

while i <= 10:
    print(i * i, end=' ')
    i += 1


i = 1
N = 10
x = 1

while i <= 10:
    print(x, end=' ')
    i += 1
    x += 1
    x = i ** 2
    

#print from N to 1
N = 5
i = 5

while i >= 1:
    print(i, end=' ')
    i -= 1



#print all even numbers from N to 1
N = int(input())

if N % 2 == 0:
    i = N
else:
    i = N - 1

while i >= 2:
    print(i, end=' ')
    i -= 2



#working with testcases
#Read an integer T from input. Then take T more inputs containing one integer each.
#print the square of these integers
T = int(input())
i = 1

while i <= T:
    n = int(input())
    print(n ** 2)
    i += 1