import math


def stddev(times):
    average = lambda lst: sum(lst) * 1.0 / len(lst)
    avg = average(times)
    return math.sqrt(average([(x - avg)**2 for x in times]))



def radixSort(array):
    """


    :param array:
    :return:
    """
    tmp = list(array)

    for shift in xrange(0, 32, 8):

        counts = [0] * 0x100
        for x in array:
            counts[(x >> shift) & 0xFF] += 1

        buckets = []
        cnt = 0
        for c in counts:
            buckets.append(cnt)
            cnt += c

        for x in array:
            b = (x >> shift) & 0xFF
            tmp[buckets[b]] = x
            buckets[b] +=1

        array, tmp = tmp, array
    return array



import random

if __name__ == '__main__':
    array = [random.randint(1,2**32) for f in xrange(10000)]

    sortedArray = radixSort(array)
    print sortedArray
    print max(sortedArray)
    print min(sortedArray)
