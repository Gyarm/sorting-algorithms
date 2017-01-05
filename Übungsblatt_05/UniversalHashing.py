class HashFunction:
    def __init__(self, a, b, p, u, m):
        self.__a = a
        self.__b = b
        self.__p = p
        self.__u = u
        self.__m = m

    # getter methods for members
    def __getA(self):
        return self.__a

    def __getB(self):
        return self.__b

    def __getP(self):
        return self.__p

    def __getU(self):
        return self.__u

    def __getM(self):
        return self.__m

    a = property(__getA)
    b = property(__getB)
    p = property(__getP)
    u = property(__getU)
    m = property(__getM)

    def set_random_parameters(self):
        import random
        self.__a = random.randrange(1, self.__p, 1)
        self.__b = random.randrange(0, self.__p, 1)

    def apply(self, x):
        return ((self.__a * x + self.__b) % self.__p) % self.__m


# computes mean bucket size for a given hash function h and set S
def mean_bucket_size(S, h):
    # dictionary that holds the number of each calculated HashKey
    keyOccurences = {}
    for key in S:
        hashKey = h.apply(key)
        keyOccurences[hashKey] = keyOccurences.get(hashKey, 0) + 1
    return sum(keyOccurences.values())/len(keyOccurences)


# gets the minimal c from 1000 calculated hash tables
def estimate_c_for_single_set(S, h):
    import sys
    # quality of c depending on how small meanBucketSize is
    # therefore we calculate its minimum
    minimumMeanBucketSize = sys.maxsize
    for hashFunction in range(1000):
        h.set_random_parameters()
        meanBucketSize = mean_bucket_size(S, h)
        if meanBucketSize < minimumMeanBucketSize:
            minimumMeanBucketSize = meanBucketSize
    # calculate minimal c out of minimumMeanBucketSize
    # m and len(S) are constant
    return (minimumMeanBucketSize - 1) * h.m / len(S)


def create_random_universe_subset(k, u):
    import random
    # random start index
    startIndex = random.randint(0, u-k-1)
    # generate randomized key set
    Set = list(range(startIndex, startIndex + k))
    random.shuffle(Set)
    return Set


def estimate_c_for_multiple_sets(n, k, h):
    # list with c
    cValues = []

    for setIndex in range(n):
        Set = create_random_universe_subset(k, h.u)
        c = estimate_c_for_single_set(Set, h)
        cValues.append(c)

    return (sum(cValues)/len(cValues), min(cValues), max(cValues))


def test_hashing(u, m, p, n, k, h):
    print(("HashFunction: a * x + b mod {h.p} mod {h.m}\n" +
           "Size of key sets = {k} out of universe range(0,{u})\n" +
           "Number of key sets = {n}").format(**locals()))
    print("Mean\tmin\tmax")
    resTuple = estimate_c_for_multiple_sets(n, k, h)
    print(resTuple[0], resTuple[1], resTuple[2], sep='\t')


if __name__ == "__main__":
    u = 100
    m = 100
    p = 101
    n = 1000
    k = 20
    h = HashFunction(1, 2, p, u, m)

    print("-----------------------------------------------")
    print("Test with c-universal hash function:")
    test_hashing(u, m, p, n, k, h)

    print("-----------------------------------------------")
    print("Test with non-universal hash function:")
    p = 60
    h = HashFunction(1, 2, p, u, m)
    test_hashing(u, m, p, n, k, h)
