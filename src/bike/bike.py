from constants import Color, Size


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
