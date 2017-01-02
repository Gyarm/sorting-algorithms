class HashFunction:
    def __init__(self, a, b, p, u, m):
        if not (a <= p-1 and a >= 1 and
                b <= p-1 and b >= 0 and
                p > m and p > len(u)):
            del(self)
            print("Creation of HashFunction failed!")
        else:
            self.__a = a
            self.__b = b
            self.__p = p
            self.__u = u
            self.__m = m

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


def mean_bucket_size(S, h):
    # dictionary that holds the number of each calculated HashKey
    keyOccurences = {}
    for key in S:
        hashKey = h.apply(key)
        keyOccurences[hashKey] = keyOccurences.get(hashKey, 0) + 1
    print(keyOccurences)
    return sum(keyOccurences.values())/len(keyOccurences)
