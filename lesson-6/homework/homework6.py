# 1
def modify_string(txt):
    vowels = 'aeiouAEIOU'
    result = ''
    count = 0
    for i in range(len(txt)):
        result += txt[i]
        count += 1
        if count == 3:
            if txt[i] in vowels:
                result += txt[i+1]
                result += '_'
                count = 1
            elif i + 1 < len(txt):
                result += '_'
                count = 0
    return result

print(modify_string('hello'))

# 2
n = int(input('Enter n: '))
for i in range(n):
    print(i ** 2)

# 3 
# 3.1
num = 1
while num <= 10:
    print(num)
    num += 1 

# 3.2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# 3.3
n = int(input(' '))
total = sum(range(1, n + 1))
print('Sum: ', total)

# 4
num = int(input(' '))
for i in range(1, 11):
    print(num * i)

# 5
numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if n == 75 or n == 150 or n == 145:
        print(n)

# 6
num = int(input(' '))
count = 0
while num > 0:
    num //= 10
    count += 1
print(count)

# 7
for i in range(5, 0, -1):
    for n in range(i, 0, -1):
        print(n, end=' ')
    print()

# 8
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# 9
for num in range(-10, 0):
    print(num)

# 10
for num in range(5):
    print(num)
print("Done!")

# 11
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
start = 25
end = 50
print(f'Prime numbers between {start} and {end}:')
for n in range(start, end + 1):
    if prime(n):
        print(n)

# 12
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number = 5
print(f'{number}! =', factorial(number))
