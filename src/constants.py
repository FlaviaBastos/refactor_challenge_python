from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Relationship(Enum):
    BOSS = 0
    EMPLOYEE = 1
    COWORKER = 2
