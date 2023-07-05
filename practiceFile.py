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