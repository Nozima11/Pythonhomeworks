# 1
name = input("Your name: ")
year = input("Your birth year: ")
year = int(year)
print(2025-year)
print(f"Hello, {name}. Your are {year} years old.")

# 2
car_brands = ["Tesla", "Honda", "Toyota", "BMW", "Ford"]
txt = 'LMaasleitbtui'.lower()
found_brand = []
for brand in car_brands:
  brand_lower = brand.lower()
  if all(brand_lower.count(char) <= txt.count(char) for char in brand_lower):
    found_brand.append(brand)

print(found_brand)

# 3
car_brands = ["Tesla", "Honda", "Toyota", "BMW", "Ford", "Mazda"]
txt = 'MsaatmiazD'.lower()
found_brand = []
for brand in car_brands:
  brand_lower = brand.lower()
  if all(brand_lower.count(char) <= txt.count(char) for char in brand_lower):
    found_brand.append(brand)
print(found_brand)

# 4
txt = "I'am John. I am from London"
words = txt.split()
print(words[-1])

# 5
name = 'John'
print(name [::-1])

# 6
name = 'John'
print(len(name))

# 7
numbers = ['1', '98', '95', '20']
print(max(numbers))

# 8
word = input('Write a word: ')
if word == word[::-1]:
  print('This word id palindrome']
        else:
          print('This word is not palindrome')
# 9
email = input('Your email: ')
domain = email.split('@')[-1]
print(domain)

# 10
import random
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
parol = ''
for i in range (8):
    parol += random.choice(symbols)
 
print(parol)







