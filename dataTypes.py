# input
D = int(input()) # user input is always considers as string
E = int(input()) # type casting "converting from one type to other data type"
print(D+E) #prints addition of D & E

name = 'kevin'
print("hello", name)

name1 = input()
print("hello", name1)

# type
print(type(10)) #Prints type of the data

print(type(2.5)) #numbers with decimal point are float data types

print(type(True)) #Bool

print(type("hello world")) #string

type("") #string

print(type(None)) #None data type === Null


#variable naming convention
NUMBER = 10
number = 13
_number = 15
Number = 17
print(_number)
number_of_trees = 10   # only "_ " is allowed as special charactor 
# 12number = 10 -> error
# &number = 10 -> error
# Keywords not cannot be variables i.e. True, False, None


# variable reassignment
x=10
y=20

x=y

print(x) # 20
print(y) # 20

a = 3
b = "hello"
num = y 
y = 5
print(num, y) #prints "hello 5"


# type casting 
# str -> int
z = int("56")
print(z, type(z))

#str -> float
x = float("8.5")
print(x, type(x))

#float -> int
z  = int(4.5)
print(z, type(z)) # prints 4


#int - float
x = float(4)
print(x, type(x))


#int -> bool
b = bool(5) #prints "True" for the numbers expect "0"
print(b, type(b))

b = bool(0)
print(b, type(b)) #prints "False"


#float -> bool
b = bool(0.4)
print(b, type(b))

b = bool(-6.9)
print(b, type(b))

b = bool(0.0)
print(b, type(b))


#int -> str
s = str(10)
print(s, type(s))


#bool -> int
print(int(True)) #print 1
print(int(False)) #prints 0


#str -> bool
print(bool("hello")) #prints TRUE
#All strings converted to "Bool" gives TRUE, except empty str ""
print(bool("")) #prints FALSE
print(bool(None)) #Prints TRUE










