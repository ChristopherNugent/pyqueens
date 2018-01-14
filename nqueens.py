import argparse


def lazy_n_queens(n):
    pstack = []
    pstack.append([])
    while(pstack):
        cur = pstack.pop()
        if len(cur) == n:
            yield cur
            continue
        for pos in range(n):
            cur.append(pos)
            if check_partial(cur):
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
