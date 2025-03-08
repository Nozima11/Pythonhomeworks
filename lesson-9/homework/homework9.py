# 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
r = float(input('radius: '))
c = Circle(r)

print('area: ', c.area())
print('perimeter: ', c.perimeter())

# 2
from datetime import date

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year

name = input('Name: ')
country = input('Country: ')
birth_year = int(input('Birth year: '))

p = Person(name, country, birth_year)

print('Name:', p.name)
print('Country:', p.country)
print('Age:', p.age())


