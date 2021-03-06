from constants import Relationship


class Research:
    """Creates a research object.

    Args:
        relationships (list[Relationship objects]): list of relationships to be searched.
    """

    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[1] == Relationship.BOSS:
                print(f"{r[0].name} has an employee {r[2].name}.")
