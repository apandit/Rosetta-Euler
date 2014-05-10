#!/usr/bin/python

import itertools

def Poly(n):
    p3 = n * (n + 1) / 2
    p4 = n * n
    p5 = n * (3*n - 1) / 2
    p6 = n * (2*n - 1)
    p7 = n * (5*n - 3) / 2
    p8 = n * (3*n - 2)

    return p3, p4, p5, p6, p7, p8

def MakeLists():
    limit = 150 
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    func = lambda x : (1000 <= x < 10000) and (x % 100 > 9) and (x / 100 > 9)
    for i in xrange(1,limit):
        p3, p4, p5, p6, p7, p8 = Poly(i)
        if func(p3): l3.append(p3) 
        if func(p4): l4.append(p4)
        if func(p5): l5.append(p5)
        if func(p6): l6.append(p6)
        if func(p7): l7.append(p7)
        if func(p8): l8.append(p8)

    return l3, l4, l5, l6, l7, l8


# Original poly list with vals < 10000
l3, l4, l5, l6, l7, l8 = MakeLists()

mod = lambda x : x % 100
div = lambda x : x / 100

print "Permutations to check: "
print len(l3) * len(l4) * len(l5) * len(l6) * len(l7) * len(l8)
bl = [l3, l4, l5, l6, l7, l8];
for p in itertools.permutations([0, 1, 2, 3, 4, 5]):
    for x3 in bl[p[0]]: 
        for x4 in bl[p[1]]:
            if mod(x3) != div(x4):
                continue
            for x5 in bl[p[2]]:
                if mod(x4) != div(x5):
                    continue
                for x6 in bl[p[3]]:
                    if mod(x5) != div(x6):
                        continue
                    for x7 in bl[p[4]]:
                        if mod(x6) != div(x7):
                            continue
                        for x8 in bl[p[5]]:
                            if mod(x7) != div(x8):
                                continue
                            if mod(x8) != div(x3):
                                continue

                            l = [x3, x4, x5, x6, x7, x8]
                            if len(set(l)) != len(l):
                                continue

                            print "Found it: "
                            print x3, x4, x5, x6, x7, x8
                            print x3 + x4 + x5 + x6 + x7 + x8
                            exit(0)


print "Finished"
