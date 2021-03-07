from constants import Relationship


class Research:
    """Instatiate class and run a research.

    Args:
        relationships (list[Relationship objects]): list of relationships to be searched.

    Returns:
        A string listing all boss-employee relationships.
        None if the list of relationships is empty.
    """

    def __init__(self, relationships):
        if not relationships:
            print("Relationships list is empty")
            return

        relations = relationships.relations

        for r in relations:
            if r[1] == Relationship.BOSS:
                print(f"{r[0].name} has an employee {r[2].name}.")
