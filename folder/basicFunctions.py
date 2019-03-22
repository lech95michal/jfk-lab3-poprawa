def callable_(arg: str) -> str:
    """A function in another module."""
    return '! %r !' % arg


def suma(a, b) -> int:
    """Returns a sum of two arguments."""
    return a+b


def iloczyn(a, b) -> int:
    """Returns a multiplication of two arguments"""
    return a*b


def iloraz(a, b) -> int:
    """Devides numbers"""
    return a/b


def roznica(a, b) -> int:
    """Odejmuje drugą od pierwszej"""
    return a-b
