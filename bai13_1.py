def foo(x: int) -> str:
    res: str
    if x == 65:
        res = 'A'
    elif x == 66:
        res = 'B'
    elif x == 67:
        res = 'C'
    else:
        res = "haven't check"
    return res
