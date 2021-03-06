from constants import Color, Size

from retail.package import Package
from retail.book import Book
from bike.bike import Bike, BikeFilter
from people.relationships import Relationships
from people.person import Person
from people.research import Research


def package_manager():
    """Creates and uses package functions"""

    p = Package()

    p.add_item("Entry 1")
    p.add_item("Entry 2")
    print(f"Package pieces:\n{p}\n")

    file = r"package.txt"
    p.save_to_file(file)


def book_manager():
    """Creates and uses book functions"""

    b = Book()

    b.add_item("Page 1")
    b.add_item("Page 2")
    print(f"Book pages:\n{b}\n")

    file2 = r"book.txt"
    b.save_to_file(file2)


def bike_manager():
    """Creates bikes and uses bike filter function"""

    norco = Bike("Norco", Color.GREEN, Size.SMALL)
    rocky_mountain = Bike("Rocky", Color.GREEN, Size.LARGE)
    santa_cruz = Bike("SantaCruz", Color.BLUE, Size.LARGE)

    bikes = [norco, rocky_mountain, santa_cruz]

    bf = BikeFilter()
    print("Green bikes:")
    for b in bf.filter_by_color(bikes, Color.GREEN):
        print(f" - {b.name} is green")


def people_manager():
    """Creates people and their relationships and run a research"""

    boss = Person("Bob")
    employee1 = Person("Tim")
    employee2 = Person("Amy")

    relationships = Relationships()
    relationships.add_boss_and_employee(boss, employee1)
    relationships.add_boss_and_employee(boss, employee2)

    Research(relationships)


def main():
    """Calls different managers"""

    package_manager()
    book_manager()
    bike_manager()
    people_manager()


if __name__ == "__main__":
    main()
