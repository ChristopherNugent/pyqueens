import argparse
from nqueens import lazy_n_queens, print_board

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
