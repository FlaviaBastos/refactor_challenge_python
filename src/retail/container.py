class Container:
    def __init__(self):
        self.items = []
        self.count = 0

    def add_item(self, text):
        self.items.append(f"{text}")
        self.count += 1

    def remove_item(self, pos):
        del self.items[pos]

    def __str__(self):
        return "\n".join(self.items)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(str(self))
