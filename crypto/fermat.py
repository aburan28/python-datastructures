


def fermat(n):
    # is prime or not
    if n%2!=0:
        print n
        return n

    if not n & 1:
        print n
        return  False

sum = 0
for i in xrange(1000000):
    v = fermat(i)

    if v != False:
        sum += v
        print sum
