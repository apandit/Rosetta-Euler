-- Solution for Euler #1
-- @Title: Multiples of 3 and 5

-- Naive solution:
-- Recursive solution; not sure if tail-optimized
mul35 :: Integer -> Integer
mul35 n 
    | n < 3 = 0
    | pred == True = n + mul35 (n-1)
    | otherwise = mul35 (n-1)
    where pred = (mod n 3 == 0 || mod n 5 == 0)

-- Constant time solution:
-- n / 3 is number of multiples of 3, ditto with 5
-- sum of consecutive numbers: n (n+1) / 2
-- Take consecutive numbers, 1->n and multiply by m
-- You get sum of first n multiples of m
-- Subtract n / 15 multiples because of duplicates
mul35ez :: Integer -> Integer
mul35ez n = sumConsec(range3) * 3 + sumConsec(range5) * 5 - sumConsec(range15) * 15
    where
        sumConsec r = div (r * (r + 1)) 2
        range3 = div n 3
        range5 = div n 5
        range15 = div n 15

main = do {
    putStr( "Naive solution: " );
    print( mul35 999 );
    putStr( "Constant time : " );
    print( mul35ez 999 );
    }
