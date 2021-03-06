from .container import Container


class Package(Container):
    def add_item(self, text):
        self.items.append(f"{self.count}: {text}")
        self.count += 1
