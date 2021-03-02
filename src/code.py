from enum import Enum


class Package:
    def __init__(self):
        self.pieces = []
        self.count = 0

    def add_piece(self, text):
        self.pieces.append(f"{self.count}: {text}")
        self.count += 1

    def remove_piece(self, pos):
        del self.pieces[pos]

    def __str__(self):
        return "\n".join(self.pieces)

    def save_to_file(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()


class Book:
    def __init__(self):
        self.pages = []
        self.page_count = 0

    def add_page(self, text):
        self.pages.append(f"{text}")
        self.page_count += 1

    def remove_page(self, pos):
        del self.pages[pos]

    def __str__(self):
        return "\n".join(self.pages)

    def save_to_file(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()


p = Package()
b = Book()
p.add_piece("Entry 1")
p.add_piece("Entry 2")
print(f"Package pieces:\n{p}\n")
file = r'package.txt'
p.save_to_file(file)
b.add_page("Page 1")
b.add_page("Page 2")
print(f"Book pages:\n{b}\n")

file2 = r'book.txt'
b.save_to_file(file2)


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Bike:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class BikeFilter:
    def filter_by_color(self, bikes, color):
        for b in bikes:
            if b.color == color:
                yield b

    def filter_by_size(self, bikes, size):
        for b in bikes:
            if b.size == size:
                yield b

    def filter_by_size_and_color(self, bikes, size, color):
        for b in bikes:
            if b.color == color and b.size == size:
                yield b


norco = Bike('Norco', Color.GREEN, Size.SMALL)
rocky_mountain = Bike('Rocky', Color.GREEN, Size.LARGE)
santa_cruz = Bike('SantaCruz', Color.BLUE, Size.LARGE)

bikes = [norco, rocky_mountain, santa_cruz]

bf = BikeFilter()
print('Green bikes:')
for b in bf.filter_by_color(bikes, Color.GREEN):
    print(f' - {b.name} is green')


class Relationship(Enum):
    BOSS = 0
    EMPLOYEE = 1
    COWORKER = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    relations = []

    def add_boss_and_employee(self, boss, employee):
        self.relations.append((boss, Relationship.BOSS, employee))
        self.relations.append((employee, Relationship.EMPLOYEE, boss))


class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'Bob' and r[1] == Relationship.BOSS:
                print(f'Bob has an employee {r[2].name}.')


boss = Person('Bob')
employee1 = Person('Tim')
employee2 = Person('Amy')

relationships = Relationships()
relationships.add_boss_and_employee(boss, employee1)
relationships.add_boss_and_employee(boss, employee2)

Research(relationships)
