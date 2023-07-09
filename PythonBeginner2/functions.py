#Functions
def tea():
    print("Boil some water")
    print("add sugur & tea leaves")
    print("add some milk")
    print("heat it for few mins")
    print()

tea()

for i in range(5):
    tea()


#Arguments / Parameters
def sheldon_knock(person):
    print("knock knock knock", person)

sheldon_knock("penny")
sheldon_knock("leonard")

#famous dialogues
def speak(charactor, dialogue):
    print("character =", charactor)
    print("Dialogue =", dialogue)

#speak("joey")# gives error 
speak("joey", "how you doing?")
#speak("joey", "how you doing?", 'chandler')#gives error


#example
def square(x):
    """prints the square of a parameter that is passed"""
    print(x**2)

square(3)

#Write a function which takes one number as argument and prints its cube
def cube(num):
    print(num ** 3)

cube(4)
cube(5.6)



#Return Statement
def multiply(a, b):
    return a * b

ans = multiply(3, 5)
print(ans)


#example
def square(x):
    return x*x

def pythagoras(x, y):
    return square(x) + square(y)

print(pythagoras(3,6))


#example
def foo_bar():
    print('foo')
    return 1
    print('bar')

res = foo_bar()
print(res)



#DocStrings
help(range)
help(square)


#Keyword Arguments
def introduce_family(me, father, mother, sibling):
    print("Me =", me)
    print("father =", father)
    print("mother =", mother)
    print("sibling =", sibling)

introduce_family("Ron", "Arthur", "Molly", "Ginny")

#Keyword Argument example
introduce_family(father='Arthur', sibling='Ginny', me='Ron', mother='Molly')

def random(a, b, c, d):
    print(a, b, c, d)

#keyword argument
random(b=1, c=5, a=2, d=3)

#positional arguments
random(4, 5, 6, 9)

#positional + Keyword
random(2, 7, d=5, c=1)

#error
random(2, 3, a=4, b=7)

#error
#as soon as a keyword arg is encounters, python forgets the order
#random(a=7, b=5, 2, 1)

#example keyword arguments
print("Hello", "world", "hi", end='+-\nok')
print("Hello", "World", "hi", sep='_')


#Default Arguments
def simple_interest(p, t, r):
    return(p * r * t)

print(simple_interest(100, 1, 5))

#By default, we want the rate of interest to be 5%
#however we can get other rates as well
#example of default arg
def SI(p, t, r = 5):
    return (p * r * t)/100

print(SI(100, 2))

#overriding the defeault arg
print(SI(100, 2, 10))

#overriding default arg using keyword arg
print(SI(5, 4, r = 7))


#Create a date printing function which takes in 4 arguments
#date, month, year, style
#style 0 -> d/m/y
#style 1 -> m/d/y
#for all other, "Invalid Style"
#Default style 0
def print_date(day, month, year, style=0):
    if style == 0:
        print(day, month, year, sep='/')
    elif style == 1:
        print(month, day, year, sep='/')
    else:
        print('Invalid Style')

print(print_date(23, 11, 2023))
print(print_date(1, 5, 2022, 1))
print(print(1, 3, 9, 2023))#Invalid style


#Scope
chief_of_house = "mother"

def change_chief():
    chief_of_house = "father"
    print("Inside the function -", chief_of_house)#prints father

change_chief()
print("Outside the house -", chief_of_house)#prints mother


#example explanation
a = 10 #global variable

def a():
    a = 5 #creates new variable altogether (Local variable)
    #"a = 5" is accessible inside the block or function which this has been defined. This block of region
    #where you can access this variable is said to be its 'scope'
    print("Inside the function -", a)# prints 5

a()
print("Outside the function -", a) #prints 10









