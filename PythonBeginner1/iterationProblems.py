#Loop Problems
#PASS statement
N = 1000

if N % 100 == 0:
    pass        #Pass - it is a null statement which interperter simply 'moves over
#we use pass when your logic or code is incomplete and it should not affect the entrie file with error.
print('end of the program')


#PRINT sep
print('hello', 'world', 5, True, None, 3.4)
#Sep
print('hello', 'world', 5, True, None, 3.4, sep=' | ') #seperates each value with " | "

print("Hello", 'World', sep=',', end='+')
print('foo', sep='./')
print('Bar', end=' 123')



#Factors and Prime Numbers
#print all factors
N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i)


#count the Factors
#find prime number
N = int(input())
F = 0

for i in range(1, N+1):
    if N % i == 0:
        F += 1

print(F)
if F == 2:
    print('prime number')
else:
    print('not a prime number')



#Sum of factors
N = int(input())
F = 0

for i in range(1, N+1):
    if N % i == 0:
        F += i

print(F)



#Break
#stop or destroy a loop
for i in range(10):
    print(i, end=' ')

    if i == 5:
        break

    print("for loop continues")



#Continue statement
#skips an iteration
for i in range(10):

    if i == 5:
        continue

    print(i, end=' ')

for i in range(10):

    if i%3 == 0:
        continue

    print(i, end=' ')



#Randam Game
'''
Design a game to generate and print random numbers from 1 to 10
- you need to keep on printing till you get a 5
- skip printing multilpes of 4
'''
import random

while True:
    r = random.randint(1, 10)
    if not r % 4:
        print(r)
    if r == 5:
        break


while True:
    r = random.randint(1, 10)
    if not r % 4:
        continue
    
    print(r, end=' ')

    if r == 5:
        break

