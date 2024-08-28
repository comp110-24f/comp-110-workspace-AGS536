"""ex01: Calculate resources necessary for tea party"""

__author__ = "730771832"


def tea_bags(people: int) -> int:
    """Calculate num of tea bags based on people"""
    return people * 2


def treats(people: int) -> int:
    """Calculate num of treats based on people"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost based on num of teas and treats"""
    return tea_count * 0.5 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """Calculate and allocate resources for tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(tea_bags(guests))
    print(treats(guests))
    print(cost(tea_bags(guests), treats(guests)))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))
