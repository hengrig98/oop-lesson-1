class Cars:
    doors = 4
    wheels = 4 
    gas = True

    def __init__(self, engine, trim, color, year, condition='used') -> None:
        self.engine = engine
        self.trim = trim
        self.color = color
        self.year = year
        self.condition = condition

    def intro(self):
        print(f'Hello! this is our latest vehicle in our showroom, snappy motor with a {self.engine}!')
    

BMW = Cars('5.0 V8', 'M package', 'Black', '2018')
Audi = Cars('3.0T V6', 'S-line', 'Red', '2017')
Dodge = Cars('6.4 V8', 'Scatpack', 'White', '2020')


print(BMW.trim)
print(Audi.color)
print(Dodge.engine)
print(BMW.year)

Dodge.intro()
BMW.intro()

print(Dodge.condition)
print(BMW.condition)








# print(BMW.doors)
# print(BMW.year)
# BMW.doors = 2
# BMW.year = 1998
# print(BMW.doors)
# print(BMW.year)

# Cars.year = 2017
# print(Audi.doors)
# print(Audi.year)

