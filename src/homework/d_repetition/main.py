"""
HW04 - Menu program for repetition functions.

Menu:
1 - Factorial (valid input: 1..9)
2 - Sum odd numbers up to N (valid input: 1..99)
3 - Exit
"""

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers


def _get_int(prompt: str) -> int:
    """Safe integer input loop."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter an integer.")


def _get_int_in_range(prompt: str, low: int, high: int) -> int:
    """Prompt until an integer in [low, high] is entered."""
    while True:
        value = _get_int(prompt)
        if low <= value <= high:
            return value
        print(f"Value must be between {low} and {high} (inclusive). Try again.")


def main() -> None:
    """Run the HW04 menu loop."""
    while True:
        print("\nHomework 4 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = _get_int("Select an option (1-3): ")

        if choice == 1:
            n = _get_int_in_range("Enter a number (1..9): ", 1, 9)
            result = get_factorial(n)
            print(f"{n}! = {result}")

        elif choice == 2:
            n = _get_int_in_range("Enter a number (1..99): ", 1, 99)
            result = sum_odd_numbers(n)
            print(f"Sum of odd numbers from 1 to {n} = {result}")

        elif choice == 3:
            print("Goodbye!")
            break

        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
