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
# cannot append, remove, update operations
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

