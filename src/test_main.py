import os
import sys

import pytest

sys.path.append(os.getcwd())

from .constants import Color, Size, Relationship

from bike.bike import Bike, BikeFilter
from people.person import Person
from people.relationships import Relationships
from people.research import Research
from retail.book import Book
from retail.container import Container
from retail.package import Package


# Package Tests
def test_package_add_item():
    package1 = Package()
    package1.add_item("Entry 1")
    package1.add_item("Entry 2")

    assert package1.count == 2
    assert len(package1.items) == 2
    assert f"{package1.count - 1}: Entry 2" in package1.items


def test_package_remove_item():
    package1 = Package()
    package1.add_item("Entry 1")
    nxt_entry = package1.count
    package1.add_item("Entry 2")
    package1.add_item("Entry 3")

    assert package1.count == 3
    assert len(package1.items) == 3
    assert f"{nxt_entry}: Entry 2" in package1.items

    package1.remove_item(1)

    assert package1.count == 3
    assert len(package1.items) == 2
    assert f"{nxt_entry}: Entry 2" not in package1.items


def test_package_save_to_file():
    package1 = Package()
    package1.add_item("Entry 1")
    package1.add_item("Entry 2")
    package1.save_to_file(r"test_package.txt")

    assert os.path.exists("test_package.txt")
    assert os.path.isfile("test_package.txt")
    assert os.stat("test_package.txt").st_size != 0

    os.remove("test_package.txt")


# Book Tests
def test_book_add_item():
    book1 = Book()
    book1.add_item("Page 1")
    book1.add_item("Page 2")

    assert book1.count == 2
    assert len(book1.items) == 2
    assert f"Page 2" in book1.items


def test_book_remove_item():
    book1 = Book()
    book1.add_item("Page 1")
    book1.add_item("Page 2")
    book1.add_item("Page 3")

    assert book1.count == 3
    assert len(book1.items) == 3
    assert f"Page 2" in book1.items

    book1.remove_item(1)

    assert book1.count == 3
    assert len(book1.items) == 2
    assert f"Page 2" not in book1.items


def test_book_save_to_file():
    book1 = Book()
    book1.add_item("Page 1")
    book1.add_item("Page 2")
    book1.save_to_file(r"test_book.txt")

    assert os.path.exists("test_book.txt")
    assert os.path.isfile("test_book.txt")
    assert os.stat("test_book.txt").st_size != 0

    os.remove("test_book.txt")


# Bike Tests
def test_bike_filters():
    bike1 = Bike("Bike 1", Color.RED, Size.SMALL)
    bike2 = Bike("Bike 2", Color.BLUE, Size.SMALL)
    bike3 = Bike("Bike 3", Color.GREEN, Size.MEDIUM)
    bike4 = Bike("Bike 4", Color.RED, Size.LARGE)
    bike5 = Bike("Bike 5", Color.BLUE, Size.LARGE)

    bikes = [bike1, bike2, bike3, bike4, bike5]

    bike_filter = BikeFilter()
    filtered_color = list(bike_filter.filter_by_color(bikes, Color.BLUE))
    assert len(filtered_color) == 2
    for bike in filtered_color:
        assert bike.color == Color.BLUE

    filtered_size = list(bike_filter.filter_by_size(bikes, Size.SMALL))
    assert len(filtered_size) == 2
    for bike in filtered_size:
        assert bike.size == Size.SMALL

    filtered_color_size = list(
        bike_filter.filter_by_size_and_color(bikes, Size.LARGE, Color.RED)
    )
    assert len(filtered_color_size) == 1
    for bike in filtered_color_size:
        assert bike.size == Size.LARGE
        assert bike.color == Color.RED


# Relationship Tests
def test_relationships(capsys):
    boss = Person("Bob")
    person1 = Person("Tim")
    person2 = Person("Amy")

    relationships = Relationships()
    relationships.add_boss_and_employee(boss, person1)
    relationships.add_boss_and_employee(boss, person2)

    Research(relationships)
    captured = capsys.readouterr()

    assert len(relationships.relations) == 4
    assert (
        captured.out
        == f"Bob has an employee {person1.name}.\nBob has an employee {person2.name}.\n"
    )
