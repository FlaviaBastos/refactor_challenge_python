from .container import Container


class Package(Container):
    """Creates a package object.
    Inherits from Container.
    """

    def add_item(self, text):
        """Adds item to package and increases count.

        Args:
            text (str): item description.
        """
        self.items.append(f"{self.count}: {text}")
        self.count += 1
