from .constants import Relationship


class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == "Bob" and r[1] == Relationship.BOSS:
                print(f"Bob has an employee {r[2].name}.")
