def lazy_n_queens(n, w=0):
    """Yield all solutions to the n-queens problem"""
    pstack = []
    pstack.append([])
    while(pstack):
        cur = pstack.pop()
        for pos in get_safe_pos_list(cur, n, w):
            cur.append(pos)
            # if check_newest(cur, n, w):
            if len(cur) == n:
                yield cur, True
            else:
                pstack.append(cur[:])
                yield cur, False
            cur.pop()


def get_safe_pos_list(state, n, w):
    safe_pos_list = [True for i in range(n)]
    k = len(state)
    for i in range(k):
        if k - i >= n - w:
            continue
        j = state[i]
        safe_pos_list[j] = False
        h = k - i + j
        if h >= 0 and h < n:
            safe_pos_list[h] = False
        h = i - k + j
        if h >= 0 and h < n:
            safe_pos_list[h] = False
    return [i for i in range(n) if safe_pos_list[i]]


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


def check_newest(psol, n, weakness=0):
    """Save time by only checking of the last queen in the partial
    solution is legally placed. This is acceptable since by building
    on legal solutions, we can guarantee that all queens but the last
    are legally placed."""
    if len(psol) > n:
        return False
    y = len(psol) - 1
    x = psol[y]
    # w = max(0, y - n + weakness + 1)
    w = y - n + weakness + 1
    if w < 0:
        w = 0
    for y2 in range(w, y):
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


if __name__ == '__main__':
    count = 0
    for s in lazy_n_queens(12, 0):
        count += 1
    print('{} solutions...'.format(count))
