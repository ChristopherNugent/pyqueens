def lazy_n_queens(n):
    pstack = []
    pstack.append([])
    while(pstack):
        cur = pstack.pop()
        for pos in range(n):
            cur.append(pos)
            if check_partial(cur):
                if len(cur) == n:
                    yield cur
                pstack.append(cur[:])
            cur.pop()


def check_partial(psol):
    for y in range(len(psol)):
        x = psol[y]
        for y2 in range(y + 1, len(psol)):
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
