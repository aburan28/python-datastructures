


def multiply(x,y):
    """
    

    """
    if x.bit_length() <= 2000 or y.bit_length() <= 2000:
        return x * y
    else:
        n = max(x.bit_length(),y.bit_length())
	mid = (n + 32) // 64 * 32
	nmask = (1 << half) - 1
	xlow = x & nmask
	ylow = y & nmask
	xhigh = x >> mid
	yhigh = y >> mid
	a = multiply(xhigh,yhigh)
	b = multiply(xlow + xhigh, ylow + yhigh)
	c = multiply(xlow,ylow)
	d = b - a - c
	return (((a << half) + d) << half) + c

if __name__ == '__main__':
    import unittest
    
