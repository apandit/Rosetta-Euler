-- Solution for Euler #2
-- @Title: Even Fibonacci numbers

-- Naive solution:
-- Use accumulator; this should end up as a loop instead of being recursive
fibSumEvenTo :: (Int,Int,Int,Int) -> Int
fibSumEvenTo (acc,a,b,limit)
    | c > limit = acc
    | even c    = fibSumEvenTo(acc + c, b, c, limit)
    | otherwise = fibSumEvenTo(acc, b, c, limit)
    where
        c = a + b

main = do {
    putStr( "Naive Solution: " );
    -- Accumulator starts at 2, since it's not included by default
    print( fibSumEvenTo( 2, 1, 2, 4000000 ) );
    }
