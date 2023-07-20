#Dictinaries
#Mutable data structure
#Dictionary is a data structure which stores key value mapping

#empty Dict
d = {}
d = dict()
print(d, type(d))

menu = {
    "Dal Makhani": 300,
    "Dosa": 200,
    "Pizza": 400
}
print(menu, type(menu))

d = {
    5: 'hello',
    'ok': 'bye',
    0.2: 'hi'
}
print(d, type(d))


#Reading Values
menu = {
    "Dal Makhani": 300,
    "Dosa": 200,
    "Pizza": 400
}

print(menu["Dosa"])

#Get()
print(menu.get("Dosa"))

print(menu.get("pasta")) #prints None

#Adding
menu[None] = 5
print(menu)


#Example
#if a dish in the menu, shows its price. Otherwise, chef will charge extra for it. Show the price as 5000.
menu = {
    "Dal Makhani": 300,
    "Dosa": 200,
    "Pizza": 400
}

print(menu.get("Dosa", 5000)) #prints the price of dosa
print(menu.get("Biriyani", 5000)) #prints 5000 because briyani is not there in the list



#Updation and Addtion
avenger = {
    'name': 'Thor',
    "age": 1000,
    'weapons': ['Mjollnir', 'stormbreaker']
}

avenger['name'] = 'Thor Odinson'
print(avenger)

avenger['girlfriend'] = 'Jane Foster'
print(avenger)

avenger['weapons'].append("Thunder")
print(avenger)


#Bulk Updates
avenger = {
    'name': 'thor',
    'age': 1000,
}

avenger.update({
    'age': 1100,
    'weapon': "Mjolnir",
    'best friend': 'Heimdall'
    })
print(avenger)


#Removing Entries
menu = {
    "Dal Makhani": 300,
    "Dosa": 200,
    "Pizza": 400
}

PizzaPrice = menu.pop('Pizza')
print(menu)
print("Pizza price was", PizzaPrice)

menu = {
    "Dal Makhani": 300,
    "Dosa": 200,
    "Pizza": 400
}
del menu['Pizza']
print(menu)



#Keys() and Values()
menu = {
    "Dal Makhani": 300,
    "Dosa": 200,
    "Pizza": 400,
    "Pasta": 350,
    "Idli": 50,
}

k = menu.keys()
print(k, type(k))

v = menu.values()
print(v, type(v))

#By default, itration directly over dict it iterates over Keys
for x in menu:
    print(x, end=', ')
    print(menu[x], end=', ') #prints values




#ITEMS()
menu = {
    "Dal Makhani": 300,
    "Dosa": 200,
    "Pizza": 400,
    "Pasta": 350,
    "Idli": 50,
}

print(menu.items())

for k,v in menu.items():
    print('key = ', k)
    print('value = ', v)
    print()


#How to check if key is present in a dictinonary
menu = {
    "Dal Makhani": 300,
    "Dosa": 200,
    "Pizza": 400,
    "Pasta": 350,
    "Idli": 50,
}

print('Dosa' in menu)



#Frequency Map
#Given a list of numbers , print the frequencies of all unique values in it (in any order)
#example
#[5,5,2,5,2,6,1,3]
# 5 -> 3, 2 -> 2, 6 -> 1, 1 -> 1, 3 -> 1
a = [5,5,2,5,2,6,1,3]
freq = {}

for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print(freq)


for k,v in freq.items():
    print(k, '->', v)