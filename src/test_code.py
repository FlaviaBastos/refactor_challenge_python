import pytest
import os
from .code import (
    Package,
    Book,
    Bike,
    BikeFilter,
    Color,
    Size,
    Relationship,
    Person,
    Relationships,
    Research,
)

# Package Tests
def test_add_piece():
    p = Package()
    p.add_piece("Entry 1")
    p.add_piece("Entry 2")

    assert p.count == 2
    assert len(p.pieces) == 2
    assert f"{p.count - 1}: Entry 2" in p.pieces


def test_remove_piece():
    p = Package()
    p.add_piece("Entry 1")
    nxt_entry = p.count
    p.add_piece("Entry 2")
    p.add_piece("Entry 3")

    assert p.count == 3
    assert len(p.pieces) == 3
    assert f"{nxt_entry}: Entry 2" in p.pieces

    p.remove_piece(1)

    assert p.count == 3
    assert len(p.pieces) == 2
    assert f"{nxt_entry}: Entry 2" not in p.pieces


def test_package_save_to_file():
    p = Package()
    p.add_piece("Entry 1")
    p.add_piece("Entry 2")
    p.save_to_file(r"test_package.txt")

    assert os.path.exists("test_package.txt")
    assert os.path.isfile("test_package.txt")
    assert os.stat("test_package.txt").st_size != 0

    os.remove("test_package.txt")


# Book Tests
def test_add_page():
    b = Book()
    b.add_page("Page 1")
    b.add_page("Page 2")

    assert b.page_count == 2
    assert len(b.pages) == 2
    assert f"Page 2" in b.pages


def test_remove_page():
    b = Book()
    b.add_page("Page 1")
    b.add_page("Page 2")
    b.add_page("Page 3")

    assert b.page_count == 3
    assert len(b.pages) == 3
    assert f"Page 2" in b.pages

    b.remove_page(1)

    assert b.page_count == 3
    assert len(b.pages) == 2
    assert f"Page 2" not in b.pages


def test_book_save_to_file():
    b = Book()
    b.add_page("Page 1")
    b.add_page("Page 2")
    b.save_to_file(r"test_book.txt")

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

    bf = BikeFilter()
    filtered_color = list(bf.filter_by_color(bikes, Color.BLUE))
    assert len(filtered_color) == 2
    for bike in filtered_color:
        assert bike.color == Color.BLUE

    filtered_size = list(bf.filter_by_size(bikes, Size.SMALL))
    assert len(filtered_size) == 2
    for bike in filtered_size:
        assert bike.size == Size.SMALL

    filtered_color_size = list(
        bf.filter_by_size_and_color(bikes, Size.LARGE, Color.RED)
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
