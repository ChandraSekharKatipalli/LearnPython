#2D Lists
a = [
    [10, 20],
    [30, 40, 50], [60],
    [70, 80, 90, 100]
]

print(a[1][1])


b = [
    [10, 20],
    [30, 40],
    [50, 60]
]


#Iterating over a 2D array
a = [
    [10, 20],
    [30, 40],
    [50, 60]
]

rows = len(a)
cols = len(a[0]) 

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()


def generateMatrix(N, M):
    a = []

    for i in range(N):
        #Generate a row of size M
        #append it to 'a'
        row = [0] * M
        a.append(row)
    
    return a

print(generateMatrix(3, 2))


#Reading 2D Array Input
rows, cols = map(int, input().split())

mat = []

for i in range(rows):
    row = list(map(int, input().split()))
    mat.append(row)
print(mat)


#Sum of 2 Matrices
A = [
    [10, 20],
    [30, 40],
]

B = [
    [0, 5],
    [10, 15]
]

def sumOfMatrices(A, B):
    C = []

    rows = len(A)
    cols = len(A[0])

    C = generateMatrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]

    return C

print('C = ',sumOfMatrices(A, B))



#Transpose of a Matrix
A = [
    [10, 20, 30],
    [40, 50, 60]
]

def transposeOfMatrix(A):
    N = len(A)
    M = len(A[0])

    T = generateMatrix(M, N)

    for i in range(M):
        for j in range(N):
            T[i][j] = A[j][i]
    return T

print('T = ', transposeOfMatrix(A))



#Check Identity Matrix
A = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

def checkIdentityMatrix(A):
    R = len(A)
    C = len(A[0])

    for i in range(R):
        for j in range(C):
            if i == j and A[i][j] == 1:
                continue
            elif i != j and A[i][j] == 0:
                continue
            else:
                return False
    return True    
    
print(checkIdentityMatrix(A))
