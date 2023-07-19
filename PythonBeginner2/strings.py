#Multi Line String
mul_s = """Anything I write here 
can be written in next line
  """
print(mul_s, type(mul_s))

new_mul_s = '''Anything I write here 
can be written in next line
  '''
print(new_mul_s, type(new_mul_s))


#Length of str
s = "Hello"
print(len(s))

s = "ab  cd"
print(len(s))

#Indexing 
#same as LIST
s = 'world'
print(s[1])

for i in s:
    print(i)

for i in range(len(s)):
    print(s[i])

s = ['sahil', 'bansal']
print(s[0][-1])


#Concatination
first = 'hello'
last = 'world'
print(first + ' ' + last)

a = 'abc'
a = 'abc'*2
print(a)


#List Slicing
#same as LISTS
s = 'abcdef'
print(s[4::-1])
print(s[::-1])
print(s[1:3])
print(s[:3:-1])
print(s[-2:-5:-2])


#check palindrome
#caseSensitive
def checkPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
print(checkPalindrome('racecar'))


#working with ASCII Values
#A - Z -> 65 - 90
#a - z -> 97 - 122
#ord -> python method used to retrive a ASCII values of a character
#chr -> python method used to retrive a character of a ASCII value
print(ord('9'))
print(ord('r'))
print(ord('S'))

print(chr(100))
print(chr(65))
print(chr(7877))

l = [97, 65, 98, 68, 73]
c = ''

for i in l:
    print(chr(i), end='')
    c += chr(i)
print()
print(c)

s = 'Hello WoRld'
counter = 0

for ch in s:
    if ord(ch) >= 65 and ord(ch) <= 90:
        counter += 1
print(counter)


#Changing cases
s ='Hello'
print(s.upper())
s.upper()
print(s)
s.lower()
print(s)

s = "heLlo worLd"
s.title()

s = 'world'
print(s.isupper())
s = 'WORLD'
print(s.isupper())
s = 'world'
print(s.islower())

s = 'WORLD 23 HELLO 4456/453 (*&*())'
print(s.isupper()) #returns TRUE

s = 'Hello WoRld'
counter = 0

for ch in s:
    if ch.isupper():
        counter += 1
print(counter)


#FIND 
s = "Harry Potter and Deathly Hallows"
print(s.find('P')) #return first occurence index at which it has found the give substring
print(s.find('Ha'))
print(s.find('Hal'))
print(s.find('Pot'))
print(s.find('chandu')) #prints '-1', because its not there in the range


#COUNT
print(s.count('H'))
print(s.count('Harry'))


#IN operator
print("ha" in "Harry")
# + <- concat, in -> check if substr exist



#Immutable Nature
'''
                    Python Datatypes
Immutable Datatypes                  Mutable Datatypes
    Numbers                             Lists
    Strings                             Dictionary
    Tuples                              Sets
'''
#Immutable - Something that cannot be changed
#Mutable - Something that can be changed
#Immutable
a = 'School' # school is assigned to a
a = a + 'Bus' # Now previous connection is broken and new connection is created in the memory pool
# previous 'school' is collected by Garbage collecter. Since its not used
#example
a = 'Hello'
print(id(a)) #prints the address
a += ' World'
print(id(a)) #different address 
#CRUD operation cannot be done on a string because its Immutable


#Replace
s = "Hello World"
print(s.replace('Hello', 'Hi'))

s = 'one one two two three three one'
t = s.replace('one', '1', 2) # replaces one with 1 upto 2 occurance
print(t)


#STRING to LIST
s = 'hello'
l = list(s)
print(l)


#LIST to STRING
s = 'hello'
result = ''

for i in s:
    result += i+'_'
print(result)
result = result[:-1]
print(result)

val = list(s)
print(val)
result = '_'.join(val)
print(val)



#Reversw words in a string
s = 'are you as clever as I am'
l = s.split()
val  = s.split()[::-1]
s = ' '.join(val)
print(s)
l.reverse()
print(l)



#DOT format method
a = 5
o = 4
s = "I have {} apples and {} oranges".format(a, o)
print(s)



#F-STRING
s = f"I have {a} apples and {o} oranges"
print(s)
