#Arithmetic Operators
print(3.0 + 1) # prints 4.0
'''
int + int -> int
float + int -> float
int + float -> float
float + float -> float
int / int -> float
'''
print(5 / 2) #prints float = 2.5

#Integer division
print(5 // 2) #prints only integar value (Floor Division) = 2
#[3.1] = 3
#[2.5] = 2
#[-2.6] = -3
#[4.999] = 4


#Exponents
print(2 ** 4) # x ** y "** - used to exponents"
print(10 ** -1) #negative exponent


#Modulo Operator
print(10 % 3) #prints the reminder of a division
#Modulo with decimal numbers are POSSIBLE where other languages dont support


#Operator Precedence - BEDMAS Rule
#Brackets Exponents Division Multiply Add Sub
print(10 - 4 * 2 + 6 - 4 / 2 + 3 ** 3)

x = 11
y = 2
z = 4
res = (x + y + z) ** (x % z)
print(res)



#Relational Operators
#< > <= >= == !=
#gives Bool result
print(5>2) #prints true
print(2 <= 10) #prints true
print(5 <= 5) #true
print(5>5) #false
print(5 != 5) #false
print(5 == 5) #true



