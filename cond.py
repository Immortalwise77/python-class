# Conditional Statement

age = 25
name = 'Vine'

if age < 30:
    print('Young adult')
if name == 'Bola Ahmed':
    print('let him write himself of')
if name == 'Yosuf':
    print('welcom user')
else:
    print('this user is an imposter')



# Condition && Logical Operator

num1,num2 = 10, 15

if num1 <= 10 and num2 <=13:
    print('Your values went hrough')

elif num1 >=9 or num2 >= 17:
    print('Yes')    
else:
    print('Our code wasn/t able to execute')

if num1 <=10 or num2 <=13:
    print('Holla')
else:
    print("Ignore")    

text = 'user'
last = 'Flow'

if (text == 'user' and last != 'play') and (text != 'bay' and last == 'flow'.title()):
    print('it is coresponding')

if (text == 'user' and last != 'play') or (text != 'bay' or last == 'flow'.title()):
    print('yes it works')
else:
    print('very very wrong')  

# Conditions && Bitwise Operators
n1 = 10
n2 = 12

print(n1 |n2)
if (n1 | n2) ==14:
    print('that is the value')