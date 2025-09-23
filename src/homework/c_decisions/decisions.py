def get_letter_grade_if(numerical_grade: int | float) -> str:
    """
    Returns A/B/C/D/F for a numeric grade 0..100.
    Raises ValueError if out of range so the menu can handle it.
    """
    try:
        n = int(numerical_grade)
    except (TypeError, ValueError):
        raise ValueError("Grade must be a number")

    if n < 0 or n > 100:
        raise ValueError("Grade must be between 0 and 100")

    if 90 <= n <= 100:
        return "A"
    elif 80 <= n <= 89:
        return "B"
    elif 70 <= n <= 79:
        return "C"
    elif 60 <= n <= 69:
        return "D"
    else:
        return "F"


def get_letter_grade_switch(numerical_grade: int | float) -> str:
    """
    Same logic using Python's match/case (switch-style).
    """
    try:
        n = int(numerical_grade)
    except (TypeError, ValueError):
        raise ValueError("Grade must be a number")

    if n < 0 or n > 100:
        raise ValueError("Grade must be between 0 and 100")

    match n:
        case n if 90 <= n <= 100:
            return "A"
        case n if 80 <= n <= 89:
            return "B"
        case n if 70 <= n <= 79:
            return "C"
        case n if 60 <= n <= 69:
            return "D"
        case _:
            return "F"


get_letter_grade = get_letter_grade_if
