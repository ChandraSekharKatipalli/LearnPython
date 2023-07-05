#Star Pattern
#Given N = 4, print below star pattern
'''
****
***
**
*
'''
N = 4

for i in range(4, 0, -1):
    for j in range(i):
        print('*', end='')
    print()


for i in range(1, N+1):
    for j in range(N-i+1):
        print('*', end='')
    print()


#2
N = 5

for i in range(1, N+1):
    print('*', end='')
    for j in range(N-2):
        print(" ", end='')
    print('*')


#3 Mirror stair
N = 5

for i in range(1, N+1):
    for j in range(N-i):
        print(" ", end='')
    for j in range(i):
        print("*", end='')
    print()


#4
N = 5

for i in range(1, N+1):
    for j in range(N-i):
        print(" ", end='')
    for j in range(2*i-1):
        print("*", end='')
    print()


#5
N = 11

for i in range(1, N+1):
    for j in range(N-i):
        print("_", end='')
    for j in range(1):
        print("*", end='')
    for j in range(i-1):
        print('_*', end='')
    print()

#6
N = 5

for i in range(1, N+1):
    for j in range(N-i+1):
        print("*", end='')
    for j in range(i*2-2):
        print("_", end='')
    for j in range(N-i+1):
        print('*', end='')
    print()


#7
N = 5

for i in range(1, N+1):
    for j in range(i):
        print("*", end='')
    for j in range(2*N-2*i):
        print("_", end='')
    for j in range(i):
        print('*', end='')
    print()


#8
N = 5

for i in range(1, N+1):
    for j in range(N-i+1):
        print("*", end='')
    for j in range(i*2-2):
        print("_", end='')
    for j in range(N-i+1):
        print('*', end='')
    print()
for i in range(1, N+1):
    for j in range(i):
        print("*", end='')
    for j in range(2*N-2*i):
        print("_", end='')
    for j in range(i):
        print('*', end='')
    print()

#9
N = 6

for i in range(N):
    print('*', end='')
print()
for i in range(1, N-1):
    print('*', end='')
    for j in range(N-i-2):
        print(" ", end='')
    print('*')
print('*')


#10
N = 5

for i in range(1, N+1):
    for j in range(1, i+1):
        if j % 2 == 1:
            print(j, end='')
        else:
            print(" ", end='')
    print()