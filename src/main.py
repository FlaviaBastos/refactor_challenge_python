from constants import Color, Size

from bike.bike import Bike, BikeFilter
from people.person import Person
from people.relationships import Relationships
from people.research import Research
from retail.book import Book
from retail.package import Package


def package_manager():
    """Creates and uses package functions."""

    package1 = Package()

    package1.add_item("Entry 1")
    package1.add_item("Entry 2")
    print(f"Package pieces:\n{package1}\n")

    file = r"package.txt"
    package1.save_to_file(file)


def book_manager():
    """Creates and uses book functions."""

    book1 = Book()

    book1.add_item("Page 1")
    book1.add_item("Page 2")
    print(f"Book pages:\n{book1}\n")

    file = r"book.txt"
    book1.save_to_file(file)


def bike_manager():
    """Creates bikes and uses bike filter function."""

    norco = Bike("Norco", Color.GREEN, Size.SMALL)
    rocky_mountain = Bike("Rocky", Color.GREEN, Size.LARGE)
    santa_cruz = Bike("SantaCruz", Color.BLUE, Size.LARGE)

    bikes = [norco, rocky_mountain, santa_cruz]

    bike_filter1 = BikeFilter()
    print("Green bikes:")
    for bike in bike_filter1.filter_by_color(bikes, Color.GREEN):
        print(f" - {bike.name} is green")


def people_manager():
    """Creates people and their relationships and run a research."""

    boss = Person("Bob")
    employee1 = Person("Tim")
    employee2 = Person("Amy")

    relationships = Relationships()
    relationships.add_boss_and_employee(boss, employee1)
    relationships.add_boss_and_employee(boss, employee2)

    Research(relationships)


def main():
    """Calls different managers."""

    package_manager()
    book_manager()
    bike_manager()
    people_manager()


if __name__ == "__main__":
    main()
