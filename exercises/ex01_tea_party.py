"""ex01: Calculate resources necessary for tea party"""

__author__ = "730771832"


def main_planner(guests: int) -> None:
    """Calculate and allocate resources for tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculate num of tea bags based on people"""
    return people * 2


# error during first submission: "must use key word argument"
# why use key word arguments? you can define arguments out of order by naming the parameter then assigning a value
# argument is identifiable by the parameter name "people"
# https://www.ibiblio.org/swaroopch/byteofpython/read/keyword-arguments.html#:~:text=There%20are%20two%20advantages%20%2D%20one,parameters%20have%20default%20argument%20values.


def treats(people: int) -> int:
    """Calculate num of treats based on people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost based on num of teas and treats"""
    return tea_count * 0.5 + treat_count * 0.75


# must be placed at end bc main_planner and functions called inside main_planner aren't defined yet
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
