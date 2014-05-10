#!/usr/bin/python


def NumRectangles(m,n):
    return m * (m + 1) * n * (n + 1) / 4

def IterNums():
    compare = 2 * 10**6
    (m,n) = (37, 37)
    diff = abs(compare - NumRectangles(m,n))
    for i in xrange(1,2000):
        for j in xrange(1,2000):
            tmp = NumRectangles(i,j)
            tmpDiff = abs(compare - tmp)
            if tmpDiff < diff:
                diff = abs(compare - tmp)
                m, n = i, j

            if tmp > compare and tmpDiff > diff:
                break

    return m, n, diff, m * n, NumRectangles(m,n)

print IterNums()
