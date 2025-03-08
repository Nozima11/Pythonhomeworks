# 1
def leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            if year % 100 == 0:
                return True
            else: 
                return False
        else: 
            return True
    else: 
        return False
print(leap(2024))

# 2
def number(n):
    if n % 2 == 1:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not weird')
    elif 6 <= n <= 20:
        print('Weird')
    else:
        print('Not weird')

n = int(input( ).strip())
number(n)

a = int(input('a: '))
b = int(input('b: '))
if a % 2 == 1:
    a+=1
if b % 2 == 1:
    b-=1

even_numbers = list (range(a, b + 1, 2))
print(even_numbers)

a = int(input('a: '))
b = int(input('b: '))

e_numbers = list(range(a+ (a%2), b-(b%2)+1,2))
print(e_numbers)
