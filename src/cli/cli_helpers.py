def validate_date_format(date_string):
    """
    Validate the date format.

    Args:
        date_string (str): Date in string format.

    Returns:
        bool: True if the format is valid, otherwise False.
    """
    from datetime import datetime
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False