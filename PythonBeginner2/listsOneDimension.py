#Lists
runs = []
print(runs, type(runs))

runs = [78, 90, 34, 68]
print(runs, type(runs))

movies = ['batman', 'harry potter', ['thor', 'iron man', 300, 2.0]]
print(movies)


#Length of the list
print(len(runs))
print(len(movies)) #prints 5


#Indexing
print(runs[3])
#last element
print(runs[len(runs) - 1])
#len of inner list
marvel = movies[2]
print(marvel)
print(len(marvel))
print(len(movies[2]))
#printing a element in inner list
print(marvel[0])
print(movies[2][0])


#Negative Indexing
print(runs[-1], runs[-2], runs[-3], runs[-4])
#last element
print(runs[-1])

#changing values in the list
a = [10, 20, 30]
a[0] = 50
print(a)
a[1] = a[1] + 30
print(a)
a[-1] = a[-2] + a[-3]
print(a)



#CRUD
#Create Read Update Delete
#Data Inseration
a = [5, 1, 9]
a.append(10) #Adds data at the end of the list
print(a)
#insert(index, data)
a.insert(2, 15) #inserts data at index position "2" is the index position
print(a)
a.insert(-2, 100)
print(a)
#extend(list/iterable) #takes data from the new list and appends in original list
b = [10, 20, 30]
c = [80, 90]
b.extend(c)
print(b)
#concatination
d = b + c
print(b)
b = b + c
print(b)



#Iteration over lists
l = [10, 20, 30, 40]

for i in l:
    print(i)

for i in range(len(l)):
    print(l[i], end='')

#print only odd elements in the list
for i in range(len(l)):
    if l[i] % 2 == 1:
        print(l[i], end=' ')

#Create Separate list of odd numbers
a = [7, 8, 9, 5, 1, 4]
b = []
N = len(a)

for i in range(N):
    if a[i] % 2 == 1:
        b.append(a[i])
print(b)




#Given a list of numbers, compute their
#sum
nums = [6, 8, 1, 3, 12, 15, -4, 0, 3]
sumOfNums = 0
sumOfNum = 0

print(sum(nums))

for i in nums:
    sumOfNums = sumOfNums + i
print(sumOfNums)

for i in range(len(nums)):
    sumOfNum += nums[i]
print(sumOfNum)

#Maximum
print(max(nums))

maxVal = nums[0]

for i in range(len(nums)):
    if nums[i] > maxVal:
        maxVal = nums[i]
print(maxVal)

#Average
print(sumOfNums/len(nums))

#minimum
minVal = nums[0]

for i in range(len(nums)):
    if nums[i] < minVal:
        minVal = nums[i]
print(minVal)