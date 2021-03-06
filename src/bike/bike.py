from constants import Color, Size


class Bike:
    """Creates a bike object.

    Args:
        name (str): name of the bike.
        color (enum): color of the bike.
        size (enum): size of the bike.

    """

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class BikeFilter:
    """Creates a bike filter"""

    def filter_by_color(self, bikes, color):
        """Filters bikes by color.

        Args:
            bikes (list[str]): list of bikes.
            color (enum): color of the bike.

        Yields:
            bike object that matches filter option.
        """

        for bike in bikes:
            if bike.color == color:
                yield bike

    def filter_by_size(self, bikes, size):
        """Filters bikes by size.

        Args:
            bikes (list[str]): list of bikes.
            size (enum): size of the bike.

        Yields:
            bike object that matches filter option
        """

        for bike in bikes:
            if bike.size == size:
                yield bike

    def filter_by_size_and_color(self, bikes, size, color):
        """Filters bikes by color.

        Args:
            bikes (list[str]): list of bikes.
            size (enum): size of the bike.
            color (enum): color of the bike.

        Yields:
            bike object that matches filter option.
        """

        for bike in bikes:
            if bike.color == color and bike.size == size:
                yield bike
