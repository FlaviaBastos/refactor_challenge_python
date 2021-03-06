from .constants import Relationship


class Relationships:
    relations = []

    def add_boss_and_employee(self, boss, employee):
        self.relations.append((boss, Relationship.BOSS, employee))
        self.relations.append((employee, Relationship.EMPLOYEE, boss))
