def verify(isbn: str):
    l: int = len(isbn)
    if l != 10 and l != 13:
        return False

    t = 0
    s = 0
    i = 0
    for c in isbn:
        if c is "-":
            continue
        i += 1
        if c.isdigit():
            t += int(c)
        elif c == "X" and i == 10:
            t += 10
        else:
            return False

        s += t

    return s % 11 == 0
