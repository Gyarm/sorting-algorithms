#!/usr/bin/env python3
# coding=<UTF-8>
import zipfile
import operator
import sys


def read_info_from_file(line):
    if line[0] == '#':
        return

    arr = line.split('\t')
    if (arr[6] == 'P') & (int(arr[14]) > 0):
        return arr[1]


def compute_most_frequent_city_names_by_map(filename):
    """ Gets city names from zipped text file and
    counts unique occurences by using dictionary.

    >>> compute_most_frequent_city_names_by_map(AT)
    Traceback (most recent call last):
        ...
    NameError: name 'AT' is not defined

    >>> compute_most_frequent_city_names_by_map(88)
    Traceback (most recent call last):
        ...
    ValueError: Filename must be of type String

    >>> compute_most_frequent_city_names_by_map("TestData")
    ... #doctest: +NORMALIZE_WHITESPACE
    Mooshöhe\t3
    Gmünd\t2
    Blabergalm\t1

    >>> compute_most_frequent_city_names_by_map("Austria")
    Error while processing file.
    """
    # input handling
    if type(filename) != str:
        raise ValueError("Filename must be of type String")

    cities = {}
    try:
        with zipfile.ZipFile(filename + ".zip") as z:
            with z.open(filename + ".txt") as f:
                for line in f:
                    info = read_info_from_file(line.decode('utf8'))
                    if info is not None:
                        if info in cities:
                            cities[info] += 1
                        else:
                            cities[info] = 1
    except:
        print("Error while processing file.")
        return
    sorted_cities = sorted(cities.items(),
                           key=operator.itemgetter(1), reverse=True)

    for top in range(0, 3):
        pair = sorted_cities.pop(0)
        print(pair[0] + "\t" + str(pair[1]))
        if len(sorted_cities) == 0:
            break


def compute_most_frequent_city_names_by_sorting(filename):
    """ Gets city names from zipped text file and
    counts unique occurences by sorting.

    >>> compute_most_frequent_city_names_by_sorting(AT)
    Traceback (most recent call last):
        ...
    NameError: name 'AT' is not defined

    >>> compute_most_frequent_city_names_by_sorting(88)
    Traceback (most recent call last):
        ...
    ValueError: Filename must be of type String

    >>> compute_most_frequent_city_names_by_map("TestData")
    ... #doctest: +NORMALIZE_WHITESPACE
    Mooshöhe\t3
    Gmünd\t2
    Blabergalm\t1

    >>> compute_most_frequent_city_names_by_sorting("Austria")
    Error while processing file.
    """
    # input handling
    if type(filename) != str:
        raise ValueError("Filename must be of type String")

    cities = []
    try:
        with zipfile.ZipFile(filename + ".zip") as z:
            with z.open(filename + ".txt") as f:
                for line in f:
                    info = read_info_from_file(line.decode('utf8'))
                    if info is not None:
                        for city in cities:
                            if info == city[0]:
                                city[1] += 1
                                break
                        else:
                            cities.append([info, 1])
    except:
        print("Error while processing file.")
        return
    sorted_cities = sorted(cities, key=operator.itemgetter(1), reverse=True)
    for top in range(0, 3):
        pair = sorted_cities.pop(0)
        print(pair[0] + "\t" + str(pair[1]))
        if len(sorted_cities) == 0:
            break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Function takes 1 argument: filename")
    else:
        compute_most_frequent_city_names_by_sorting(sys.argv[1])
