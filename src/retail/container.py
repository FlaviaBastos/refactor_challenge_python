class Container:
    """Creates a container object."""

    def __init__(self):
        self.items = []
        self.count = 0

    def add_item(self, text):
        """Adds item to container and increases count.

        Args:
            text (str): item description.
        """

        self.items.append(f"{text}")
        self.count += 1

    def remove_item(self, pos):
        """Removes item from container at given position.

        Args:
            pos (int): 0-indexed position of item to be removed.
        """

        del self.items[pos]

    def __str__(self):
        return "\n".join(self.items)

    def save_to_file(self, filename):
        """Saves object content to file.

        Args:
            filename (str): name of the file.
        """

        try:
            with open(filename, "w") as file:
                file.write(str(self))
        except IOError:
            print(f"Could not write file {filename}")
