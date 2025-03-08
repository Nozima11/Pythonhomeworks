#1.1
try:
    n = int(input(''))
    result = n / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')

#1.2
try:
    n = int(input(''))
except ValueError:
    print('Value error')

# 3
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found!')

# 4
try:
    n1 = input(' ')
    n2 = input(' ')
    result = float(n1) + float(n2)
    print("Sum:", result)
except ValueError:
    print('Value error')

# 5
try:
    with open('file.txt', 'w') as file:
        file.write('hello')
except PermissionError:
    print('Permission error')

# 6
list = [1, 2, 3]
try:
    print(list[5])
except IndexError:
    print('Index is out of range')

# 7
try:
    n = input(' ')
    print(' ', n)
except KeyboardInterrupt:
    print('Key board interrupt error')

# 8
try:
    result = 10 / 0
except ArithmeticError:
    print('Arithmetic error')

# 9
try:
    n = 10
    n.append(5)
except AttributeError:
    print('Attribute error')
