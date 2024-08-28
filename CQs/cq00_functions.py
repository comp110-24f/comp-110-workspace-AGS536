"""My first CQ in COMP110"""

__author__ = "730771832"


def mimic(message: str) -> str:
    """Repeats string in argument back to user"""
    return message


def main() -> None:
    """Test the function we wrote previously"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
