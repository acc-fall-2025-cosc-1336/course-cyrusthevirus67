
from src.homework.c_decisions.decisions import (
    get_letter_grade_if,
    get_letter_grade_switch,
)

print("MAIN MENU\n")
print("1-Letter grade using if")
print("2-Letter grade using switch")
print("3-Exit\n")

choice = input("Choose an option (1-3): ").strip()

if choice in {"1", "2"}:
    raw = input("Enter a grade (0-100): ").strip()
    try:
        n = int(raw)
    except ValueError:
        print("Invalid input. Please enter a whole number between 0 and 100.")
    else:
        if not (0 <= n <= 100):
            print("The number is out of range.")
        else:
            if choice == "1":
                print("Letter grade:", get_letter_grade_if(n))
            else:
                print("Letter grade:", get_letter_grade_switch(n))
elif choice == "3":
    print("Goodbye.")
else:
    print("Invalid option.")
