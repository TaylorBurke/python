def equal(a, b, c):
    if a == b and a == c or b == c and b == a or c == a and c == b:
        return 3
    if a == b or b == c or c == a:
        return 2
    return 0
