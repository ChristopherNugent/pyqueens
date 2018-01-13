import argparse


def lazy_n_queens(n):
    pstack = []
    pstack.append([])
    while(pstack):
        cur = pstack.pop()
        if check_partial(cur) and len(cur) == n:
            yield cur
            continue
        for pos in range(n):
            cur.append(pos)
            if check_partial(cur):
                pstack.append(cur[:])
            cur.pop()


def check_partial(psol):
    for col, row in enumerate(psol):
        for col2, row2 in enumerate(psol[col + 1:]):
            col2 += col + 1
            if row == row2:
                return False
            if row2 == row + (col2 - col) or row2 == row - (col2 - col):
                return False
    return True


def print_board(sol):
    for pos in sol:
        line = ['.'] * len(sol)
        line[pos] = 'Q'
        print(' '.join(line))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('size', help='Size of board to use', type=int)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--pretty",
                        help="print board in a visual format", action="store_true")
    group.add_argument('-q', '--quiet', help='do not print solutions', action='store_true')
    parser.add_argument('-c', '--count', help='display the count with each solution',
                        action='store_true')
    args = parser.parse_args()
    try:
        count = 0
        for sol in lazy_n_queens(args.size):
            count += 1
            if args.count:
                print('Solutions so far: {}'.format(count))
            if not args.quiet:
                if args.pretty:
                    print_board(sol)
                    print()
                else:
                    print(sol)
        print('Total solutions: {}'.format(count))
    except KeyboardInterrupt:
        print('\nFound {} solutions before interrupt.'.format(count))
        print('Goodbye!')
