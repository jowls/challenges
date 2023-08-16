prob1 = sum [ x | x <- [1..999], x `rem` 3 == 0 || x `rem` 5 == 0 ]

prob2 = sum [ x | x <- takeWhile (<= 4000000) fibs, even x]
  where
    fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

num3 = 600851475143
list = [x | x <- [num3,num3-1..1], x*x <= num3]
prob3 = 
