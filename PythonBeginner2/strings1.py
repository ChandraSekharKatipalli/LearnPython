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