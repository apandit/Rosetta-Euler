#!/usr/bin/python

# uses barycentric coordinates solution
def InTri(x0, y0, x1, y1, x2, y2):
    
    # Magic area formula
    a_2a = -y1 * x2 + y0 * (-x1 + x2) + x0 * (y1 - y2) + x1 * y2
    sign = -1 if a_2a < 0 else 1

    s_2a = (y0 * x2 - x0 * y2) * sign
    t_2a = (x0 * y1 - y0 * x1) * sign


    if s_2a < 0 or t_2a < 0:
        return False
    elif (s_2a + t_2a) > (a_2a * sign) :
        return False
    else:
        return True


allLines = 0
with open("triangles.txt") as f_tri:
    allLines = [line.strip() for line in f_tri.readlines()]

print len(allLines)
p = [int(x) for x in allLines[0].split(",")]
print InTri(p[0], p[1], p[2], p[3], p[4], p[5])
p = [int(x) for x in allLines[1].split(",")]
print InTri(p[0], p[1], p[2], p[3], p[4], p[5])

ctr = 0
for line in allLines:
    p = [int(x) for x in line.split(",")]
    if InTri(p[0], p[1], p[2], p[3], p[4], p[5]):
        ctr = ctr + 1


print "Total number: ", ctr
