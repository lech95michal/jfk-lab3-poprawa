def upper(arg: str):
    """Returns argument in UPPERCASE."""
    return arg.upper()


def max(arg: int, arg2: int) -> int:
    """Returns the greater number"""
    if arg > arg2:
        return arg
    else:
        return arg2


def min(x, y) -> int:
    """Returns the smaller number"""
    if x < y:
        return x
    else:
        return y
