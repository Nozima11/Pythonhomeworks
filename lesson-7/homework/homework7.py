# 1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input(' '))
print(is_prime(number))

# 2
def digit_sum(k):
    return sum(int(digit) for digit in str(k))
n = int(input(' '))
print(digit_sum(n))

# 3
def the_powers_of_2(n):
    power = 1
    while power <= n:
        print(power, end=' ')
        power *= 2
number = int(input(' '))
the_powers_of_2(number)
