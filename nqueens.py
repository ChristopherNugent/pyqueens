def lazy_n_queens(n):
    """Yield all solutions to the n-queens problem"""
    pstack = []
    pstack.append([])
    while(pstack):
        cur = pstack.pop()
        for pos in range(n):
            cur.append(pos)
            if check_newest(cur):
                if len(cur) == n:
                    yield cur
                pstack.append(cur[:])
            cur.pop()


def check_partial(psol):
    """Check the validity of a partial or complete solution"""
    for y in range(len(psol)):
        x = psol[y]
        for y2 in range(y + 1, len(psol)):
            x2 = psol[y2]
            xdif = x2 - x
            ydif = y2 - y
            if xdif == 0 or xdif == ydif or xdif == -ydif:
                return False
    return True


def check_newest(psol):
    """Save time by only checking of the last queen in the partial
    solution is legally placed. This is acceptable since by building
    on legal solutions, we can guarantee that all queens but the last
    are legally placed."""
    y = len(psol) - 1
    x = psol[y]
    for y2 in range(y):
        x2 = psol[y2]
        xdif = x2 - x
        ydif = y2 - y
        if xdif == 0 or xdif == ydif or xdif == -ydif:
            return False
    return True


def print_board(sol):
    for pos in sol:
        line = ['.'] * len(sol)
        line[pos] = 'Q'
        print(' '.join(line))
