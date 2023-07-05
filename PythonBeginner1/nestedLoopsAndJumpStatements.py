#Nested Loops
#combine 2 numbers, X and Y such that X will in 10s place and Y at units place


X = 5
Y = 2

XY = X*10 + Y

#Reverse a number
N = 792

X = N % 10
N = N // 10
Y = N % 10
Z = N // 10
print(X, Y, Z)

#With input
N = int(input())

while N != 0:
    X = N % 10
    N = N // 10
    print(X, end= ' ')

#example
N = 120
x = 0

while N > 0:
    y = N % 10
    x = 10*x + y
    N //= 10
print(x)


#HCF Highest common factor
A = int(input())
B = int(input())
HCF = 0

for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        HCF = i
print(HCF)

#LCM Lowest Common Multiple
import math
A = int(input())
B = int(input())
GCD = 0
LCM = 0

if A == 0:
    GCD = B
else:
    GCD = math.gcd(A, B)

LCM = (A * B) // GCD
print(LCM)

#or

print(math.lcm(A, B))



#Pattern Problems
#Nested Loops
#2D arrays

#print N stars
N = int(input())

for i in range(N):
    print('*', end='')


#Print N * M stars
N = 3
M = 5

#Print N rows in total
for i in range(N):
    #for each row, we want to print M stars
    for j in range(M):
        print('*', end=' ')
    #print a new line
    print()

for i in range(2):
    for j in range(1):
        print('*', end='')
    print()


#stair pattern
N = 4

for i in range(1, N+1):
    for j in range(i):
        print('*', end=' ')
    print()



#problems
T = int(input())
i = 1

while i <= T:
    n = int(input())
    i += 1
    while n != 0:
        x = n % 10
        print(x,  end='')
        n //= 10


#2
T = int(input())
N = T
i = 1
x = 0

while T != 0:
    y = T % 10
    x = x*10 + y
    print(x)
    T //= 10
if x == N:
    print('Yes')
else:
    print('No')


#3
N = int(input())

for i in range(N):
    A = int(input())
    B = int(input())

    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            HCF = i
    
    print(HCF)


#4
N = int(input())

for i in range(N):
    A = int(input())
    B = int(input())

    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            HCF = i
    LCM = (A * B) // HCF
    print(LCM)


#5
N = int(input())

for i in range(N+1, 1, -1):
    for j in range(i):
        print(j, end=' ')
    print()


#6
N = int(input())

for i in range(1, N+1):
    for j in range(i):
        print('*', end=' ')
    print()

#7
N = int(input())

for i in range(1, N+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

#8
N = int(input())

for i in range(1, N+1):
    print('*', end='')
    for j in range(N - 2):
        print(' ', end='')
        
    print('*')

