#!/usr/bin/python

def IsBouncy(a):
    isUp = True
    isDown = True

    start = a % 10
    a /= 10
    while( a > 0 and (isUp or isDown) ):
        isUp = isUp and (a % 10) >= start
        isDown = isDown and (a % 10) <= start
        start = a % 10
        a /= 10

    return not (isUp or isDown)

# Prop bouncy is 0.9 at 21780
print `IsBouncy(14355)`
print `IsBouncy(539)`

i = 538 + 1
bCtr = 538 / 2
limit = 10**9

while( i < limit ):
    if( IsBouncy(i) ):
        bCtr = bCtr + 1

    if( (bCtr * 100) % 99 == 0 and bCtr * 100 / 99 == i ):
        print( "Eureka, found it: " + `i` )
        break
    
    i = i + 1

print "Comparison: " + `bCtr` + " vs " + `i`
print "Proportion: " + `bCtr * 1.0 / i`
print "End script"
