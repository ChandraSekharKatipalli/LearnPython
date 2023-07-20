#Tuples

#IRSO
planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto'
]

#Intern at ISRO
planets[2] = "chandu's planet"
print(planets)

#Tuples used to make a Immutable list
# cannot append/insert, remove, update operations
planets = (
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto'
)
print(planets, type(planets))

#Tuple Methods
#INDEX
t = (2, 3, 10, 'hello', [5,9],(9,0,'ok'),3)
print(t[-1])


#COUNT
print(t.count(2))

#SLICING
print(t[2:])

#Assigned a new tuple to the varible 't'
#We modified the reference of our variable 't'
#Tuple was not modified
t = (10, 20, 30)
t = t[::-1]
print(t)

#How to create a tuple
t = (10, 20, 30)

print(t, type(t))

l = ["Hello", "how", "are", "you"]
t = tuple(l)
print(t, type(t))


t2 = tuple("abc")
print(t2, type(t2)) #Prints ('a', 'b', 'c')

l2 = list("abc")
print(l2, type(l2)) #Prints ['a', 'b', 'c']

t = ("Sahil")
print(type(t)) #Prints string
# tuple should contain atleast one comma seperated value

#Range
t = tuple(range(1, 10, 2))
print(t)



t = (1, 2, [5, 6])
t[2].append(10) #this works
#t[2] = [10, 20, 30] #this will not work


#SETS -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#it uses curly brackets
#Unordered data structure
#Unique elements
s = {1, 9, 'Hello', 0.5, 4, 2}
print(s, type(s))

s = {10,20, 20, 30, 40, 40, 30}
print(s)

#Create an empty set
s= set()


#Important Methods
#ADD
s = {10, 20, 30}
s.add(60)
print(s)

s.add(10)
print(s)#prints the same set

s = {10, 20, 30, 60}
s.remove(10)
print(s) #removes 10


#IN used to search a SET
s = {10, 20, 30, 40}
print(10 in s)

print(100 in s)

#TV series recommendation
#you ask 2 frds for a TV series recommendations
A = {
    'Breaking Bad',
    'Better Call Saul',
    'Dark'
}

B = {
    'Sherlock',
    'Dark',
    'The Office'
}

#Intersection
c = A & B
c = A.intersection(B)
c = B.intersection(A)
print(c)

#Union
c = A | B
c = A.union(B)
c = B.union(A)
print(c)


#Difference
# If we want only A recommendations excluding common
C = A - B
print(C)
# if we want only B recommendations excluding commom
C = B - A
print(C)


#Symmetric Difference
# if we want both A & B recommandations excluding commons
#Union - intersection
# A ^ B
C = A ^ B
print(C)



#Count Unique
arr1 = [10, 20, 30, 40, 20, 10, 20, 20]
arr2 = [50, 60, 50]

def countUnique(arr):
    s = set(arr)
    return len(s)

def countUnique(arr):
    return len(set(arr))

print(set([10, 20, 30, 40, 20, 10, 20, 20]))

