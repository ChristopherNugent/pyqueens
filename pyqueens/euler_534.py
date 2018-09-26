import nqueens
import multiprocessing
import os
import logging
from sys import argv
from time import time


def Q(t):
    start = time()
    n, w = t
    logging.info('Running Q for N = %d, W = %d', n, w)
    count = 0
    if w == n - 1:
        count = n ** n
    else:
        count = 0
        for _ in nqueens.lazy_n_queens(n, w):
            count += 1
    logging.info('Found result %d for N = %d, W = %d in %fs',
                 count, n, w, time() - start)
    return count


def S(n):
    logging.info('Zipping arguments...')
    ns = [n] * n
    ws = [n - 1] + list(range(n - 1))
    pool_args = zip(ns, ws)
    logging.info('Arguments zipped.')
    threads = os.cpu_count()
    logging.info('Running with up to %d threads', threads)
    pool = multiprocessing.Pool(threads)
    results = pool.map(Q, pool_args)
    return sum(results)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s | %(message)s')
    n = int(argv[1])
    print('Calculating S({})...'.format(n))
    result = S(n)
    print('S({}) = {}'.format(n, result))
