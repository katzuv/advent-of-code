from datetime import datetime


def get_default_year() -> int:
    """
    :return: default year which is the current year if it's December, last year otherwise
    """
    today = datetime.today()
    current_year = today.year
    if today.month == 12:
        return current_year
    else:
        return current_year - 1
