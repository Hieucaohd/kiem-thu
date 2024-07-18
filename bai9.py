def Grade(score: int) -> str:
    res: int
    if score < 0 or score > 10:
        return 'I'
    else:
        if score >= 8:
            res = 'B'
        else:
            if score >= 6.5:
                res = 'C'
            else:
                if score >= 5:
                    res = 'D'
                else:
                    res = 'F'
    return res
