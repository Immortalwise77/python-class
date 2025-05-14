print(2+2)
print('w')
print("w")
print("how are you")
print("Pter said 'He won't be here today' ")
print('Peter said "He won\t be here today" ')


#DATA TYPES#

print(type('w'))
print(type(2+2))
print(type(11.5))
print(type(True))
print(type(11 + 5j))

#variables & Strings#

P="mr kuchi"
print (P)

c_ = 3

e4= "Hello"
_4d = "happy coding"
_v = 12
print(c_, e4, _4d)

#Concatination

greeting = "Good Afternoon " + P
print(greeting)

Book = "i have a book called" + ' ' + _4d
print(Book)

Lucky_number = "You just won a car with the lucky" + ' ' +str(_v)
print(Lucky_number)

num = f"your number is {_v}"
cd = f"you just won a car with the lucky number {_v}"
print(cd, num)
car = cd[15:18]

#Strings Method

user = 'benny'
print(user.title())
user2 = "KENNY"
print(user2.lower())
user3 ="Benny"
print(user3.title())
print(user3.casefold())
print(user.capitalize())

print(cd.index("car"))

print(cd.replace('car', 'bicycle'))


# assignment....
# create five variables
# use the three concatinating method to add them to as sentence
# Apply all the strings methods to the variable/. b 

#FORMAT METHOD
fname = "Bernard"
lname = "Jerry"
middle_name = "Andrew"

full_name = "{} {} {}".format(lname, fname, "paul" )
print(full_name)

winner = "you just won the num {}". format(40)
print(winner)
n = "Welcome to class %s %s %s" %(fname,lname,middle_name)
print(n)

number = 123.64262427243
print("This number %d is formatted to 2 decimal place" %(number))
print("This number %s is formatted to 2 decimal place" %(number))

b = "         Henry"
print(b.strip())

v = "         Kenndrie"
y = "Hope            "
print(v.lstrip())
print(y.rstrip() + " " +fname)

#COUNT
print(n.count('e'))

h = f"i hhave the number {33}"
print(h.count('3'))

#PARTITIONM

k = full_name.partition('Jerry')
print(k[1][0])

jk = "This cat of mine misbehave everyday"
print(jk.index("T"))
print(jk.partition('cat'))
ee = jk.partition('cat')
print(ee[0])
print(ee[0], ee[1])

jk2 = jk.partition('misbehave')
print(jk2[1][3:5])

#SPLIT
js = "i have a bicycle"
yy = js.split()

print(yy)
print(yy[1])

#{1,2,3,4} set

#FIND
print(js.find('bicycle'))

#INTEGERS

n=1
b=2
#NUMBR ARITHEMATIC

print(n+b) # ADDITION
print(b-n) # Substraction
print(15/3)# Division
print(2*5) # Multiplication
print(15//3) # Foor division
print(15%2)# Modulus
print(2**5) # Power multiplication
nn = -34
print(abs(nn)) #  (absolute) changing the negative to positive

print(pow(2,5))

print(15*7.4)

print(11, + 5j + 2)
cx= (12.3 + 11j) * 3

bx = 11.345667788888888
print(round(bx, 3))

# Operators
# Arithematic Operator
# Comparison Operator
# Assignment Operato

name = "Jack"
text = "Today is wednesday"
print(name== "Paul") # equals to 
print(name != "Paul") # not equals to
print('is' in text) # Membership

num1, num2, num3, = 10,12, 10
print(num1 < num2)

#Assignment Operator

n = 20
print(n)
n += 5
print(n)

b = "Blessing"
b += " "+ "Henry"
print(b)

cal = 40
cal -= 10
print(cal)

div = 33
div /=3
print(div)

mod = 45
mod %= 5
print(mod)
mul = 3
mul **= 4
print(mul)

cul = 4
cul *= 2
print(cul)


#Mmebership Operator
#in and not in

l =[1,2,3,4,5]
print(3 in l)
print(10 in l)
print(7 not in l)

# lOGICAL oPERATOR
# AND, Or
print( 11 > 5 and 12 < 20)
print( 10 < 3 and 20 > 10)
# TRUE AND TRUE = TRUE
# FALSE AND FALSE =FASLE
# FALSE AND TRUE  = FALSE
# FALSE AND FALSE = FALSE


print(11 > 4 or 10 > 30)
print(2 == 3 or 3 !=5)
print(10 <= 9 or 7 > 10)
#true or true = true
# True or False = true
# False  or True = True
# False or False = False

#identity Operator
print(10 is 4)
print("henry" is  'Henry')
print('John' is not 'JOHN')

#Bitwise Operator
a = 10
b = 15
 # | bitwise or
 # & bitwise and
 # ^ bitwise xor
 # ~ bitwise not
 # << bitwise left shift
 # >> bitwise right shift

 # bitwise or (|)
# Returns 1 if atleast one bit is 1, otherwise 0

print(a | b)

# a = 1010
# b = 1111
# 1111


c = 3
d = 5
print(3 |5)
# C = 11
# d = 101
# 111 = 7

# bitwise and (&0
# returns 1 if both sides are 1, else 0


print(c & d)
# 11
# 101
# 0  0 1

e = 7
g = 12
print(e & g)

# 0111
# 1100
# 0100

# BITWISE XOR (^)
# Returns 1 if the bits are difrent, otherwise 0
print(c ^ d)
 # 011
 # 101
 # 110

 # bitwise not (~)
 # it inverts all the bits ( 1 becomes 0, 0 beccomes 1)
print(~c)
 # 011
 # 100
print(~d)
 # 101
 # 010

 #Left shift (<<)
# ''''shifts bits to the left, filling with zero on the right.  ffectively multiplies by power of any number 
 # d = 5, 101
 # d >> 2
 # 10100
print(5 << 2)

print(bin(c))
print(bin(~c))

 # c = 0000 0011
 # - = (1111 1100 + 1)
 # 1111 1101

#

 # -(x + 1)
# - x - 1

print(~20)
print(~30)
print(~0)

print(bin(22))
print(22 << 2)
print(bin(22 << 2))
print(int('00000101', 2))
print(int('00010110', 2))
 # Right Shift (>>)
# ''''shifts bits to the right, filling with zero on the left.  effectively multiplies by power of any number
 #

print(22 >> 3)
print(bin(22 >> 3))
print(5 >> 2)


print(bin(5 >> 2))
print(3 >> 3)
print(bin(33 >> 3))
print(bin(3))
#00000011
print(6 << 2)
print(2 ** 2 * 8) # Left Shift

print(8 << 2)

print(8 // (2 ** 2)) # Right Shift
print(8 >> 2)

# Octal (Base 8)

f = 30
print(oct(f))
print(int('36', 8))

# Hexadecimal (base 16)
x = 25
print(hex(x))
print(int('19', 16))

# Chr  (unique code)
(ord) = changes character back to unique code
v = 1232
print(chr(v))

print(ord('A'))
print(ord(chr(2)))
print(ord(chr(v)))
