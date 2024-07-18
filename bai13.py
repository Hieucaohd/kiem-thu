def Sum(a: list[int], n: int) -> int:
    i: int
    total = 0
    for i in range(n):
        total = total + a[i]
    return total
