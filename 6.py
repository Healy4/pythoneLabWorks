def zero(items, left, middle, right):
    if items[0] == 'AMPL':
        return left
    if items[0] == 'GAP':
        return middle
    if items[0] == 'NU':
        return right


def four(items, left, right):
    if items[4] == 'FISH':
        return left
    if items[4] == 'REXX':
        return right


def three(items, left, right):
    if items[3] == 'DM':
        return left
    if items[3] == 'TCSH':
        return right


def two(items, left, middle, right):
    if items[2] == 1969:
        return left
    if items[2] == 1965:
        return middle
    if items[2] == 1996:
        return right


def one(items, left, right):
    if items[1] == 'MASK':
        return left
    if items[1] == 'SCALA':
        return right


def main(items):
    return zero(items, one(items, three(items, four(items, 0, 1), 2), two(items, three(items, 3, 4), three(items, 3, 4), 7)
        ), 8, 9)