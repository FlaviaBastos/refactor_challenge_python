from constants import Relationship


class Relationships:
    """Creates relationships among people."""

    relations = []

    def add_boss_and_employee(self, boss, employee):
        """Creates a relationship between a boss and an employee.

        Args:
            boss (Person obj): boss object instance.
            employee (Person obj): employee object instance.

        """
        self.relations.append((boss, Relationship.BOSS, employee))
        self.relations.append((employee, Relationship.EMPLOYEE, boss))
