#!/usr/bin/env python3
# coding=<UTF-8>
import zipfile
import operator
import sys
import timeit


def read_info_from_file(filename):
    with zipfile.ZipFile(filename + ".zip") as z:
        with z.open(filename + ".txt") as f:
            for line in f:
                if line[0] == '#':
                    continue
                arr = line.decode('utf8').split('\t')
                if ('P' in arr[6]) & (int(arr[14]) > 0):
                    yield (arr[1], arr[8])


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
    [('Mooshöhe', 3), ('Gmünd', 2), ('Blabergalm', 1)]

    >>> compute_most_frequent_city_names_by_map("Austria")
    Error while processing file.
    """
    # input handling
    if type(filename) != str:
        raise ValueError("Filename must be of type String")

    cities = {}
    try:
        for city in read_info_from_file(filename):
            if city is not None:
                # .get method of dict() saves an if statement
                cities[city[0]] = cities.get(city[0], 0) + 1
    except:
        print("Error while processing file.")
        return

    sorted_cities = sorted(cities.items(),
                           key=operator.itemgetter(1), reverse=True)
    return sorted_cities


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

    >>> compute_most_frequent_city_names_by_sorting("TestData")
    ... #doctest: +NORMALIZE_WHITESPACE
    [['Mooshöhe', 3], ['Gmünd', 2], ['Blabergalm', 1]]

    >>> compute_most_frequent_city_names_by_sorting("Austria")
    Error while processing file.
    """
    # input handling
    if type(filename) != str:
        raise ValueError("Filename must be of type String")

    cities = []
    try:
        for city_tuple in read_info_from_file(filename):
            if city_tuple is not None:
                for city in cities:
                    if city_tuple[0] == city[0]:
                        city[1] += 1
                        break
                else:
                    cities.append([city_tuple[0], 1])
    except:
        print("Error while processing file.")
        return
    sorted_cities = sorted(cities, key=operator.itemgetter(1), reverse=True)
    return sorted_cities


def compute_most_frequent_city_names_by_map_DE(filename):
    # input handling
    if type(filename) != str:
        raise ValueError("Filename must be of type String")

    cities = {}
    try:
        for city in read_info_from_file(filename):
            if city is not None:
                if 'DE' in city[1]:
                    cities[city[0]] = 0
        for city in read_info_from_file(filename):
            if city is not None:
                if city[0] in cities:
                    cities[city[0]] += 1

    except:
        print("Error while processing file.")
        return

    sorted_cities = sorted(cities.items(),
                           key=operator.itemgetter(1), reverse=True)
    return sorted_cities


def compare_runtimes():
    print("Comparing runtimes:")
    print("Runtime of compute_most_frequent_city_names_by_map(\'AT\')")
    print(timeit.timeit(
         "compute_most_frequent_city_names_by_map(\'AT\')",
         number=10, globals=globals()))
    print("Runtime of compute_most_frequent_city_names_by_sorting(\'AT\')")
    print(timeit.timeit(
         'compute_most_frequent_city_names_by_sorting(\'AT\')',
         number=10, globals=globals()))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Function takes 1 argument: filename")
    else:
        print("compute_most_frequent_city_names_by_sorting('"
              + sys.argv[1] + "'):")
        sorted_cities = compute_most_frequent_city_names_by_sorting(
             sys.argv[1])
        # print result
        for top in range(0, 3):
            if len(sorted_cities) == 0:
                break
            pair = sorted_cities.pop(0)
            print(pair[0] + "\t" + str(pair[1]))

        print("compute_most_frequent_city_names_by_map('"
              + sys.argv[1] + "'):")
        sorted_cities = compute_most_frequent_city_names_by_map(sys.argv[1])
        # print result
        for top in range(0, 3):
            if len(sorted_cities) == 0:
                break
            pair = sorted_cities.pop(0)
            print(pair[0] + "\t" + str(pair[1]))

        compare_runtimes()

        print("Most frequent city names that exist in Germany as well:")
        start = timeit.default_timer()
        sorted_cities = compute_most_frequent_city_names_by_map_DE(
             "allCountries")
        end = timeit.default_timer()
        # print result
        for top in range(0, 3):
            if len(sorted_cities) == 0:
                break
            pair = sorted_cities.pop(0)
            print(pair[0] + "\t" + str(pair[1]))
        print("Runtime: " + str(end-start))
