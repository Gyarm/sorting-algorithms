#!/usr/bin/python3
import timeit
import time
import random


def get_random_list(n):
    random.seed(None)
    lst = list(range(0, n))
    random.shuffle(lst)
    return lst


def avg(lst):
    return sum(lst)/len(lst)


def quicksort(l, start, end):
    if (end - start) < 1:
        return
    i = start
    k = end
    piv = l[start]

    while k > i:
        while l[i] <= piv and i <= end and k > i:
            i += 1
        while l[k] > piv and k >= start and k >= i:
            k -= 1

        if k > i:  # swap elements
            (l[i], l[k]) = (l[k], l[i])

    (l[start], l[k]) = (l[k], l[start])
    quicksort(l, start, k - 1)
    quicksort(l, k + 1, end)


def insert_list_in_hashtable(lst):
    d = {}
    for elem in lst:
        d[elem] = 12345


if __name__ == "__main__":
    """ plots use gnuplot command:
    gnuplot -e "set logscale x 2; \
    plot 'runtimes.txt' using 1:2 with lines title 'sort',\
    '' using 1:3 with lines title 'insert'; pause -1;"
    """
    n = 2  # start with small number of int values
    while True:
        starttime = time.time()

        s = timeit.Timer('quicksort(lst, 0, len(lst)-1)',
                         setup='lst = get_random_list(n)',
                         globals=globals())
        result_time_sort = s.repeat(number=1)

        d = {}
        i = timeit.Timer('insert_list_in_hashtable(lst)',
                         setup='lst = get_random_list(n)',
                         globals=globals())
        result_time_insert = i.repeat(number=1)

        print("{0}\t{1}\t{2}".format(
            n,
            avg(result_time_sort),
            avg(result_time_insert)
        ))

        if (time.time() - starttime) > 60:
            break
        else:
            n = n * 2
            starttime = time.time()
