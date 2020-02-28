--1
myLast :: [a] -> a
myLast (x:[]) = x
myLast (x:xs) = myLast xs

--2
myButLast :: [a] -> a
myButLast (x:y:[]) = x
myButLast (x:y:xs) = myButLast (y:xs)

--3
elementAt :: [a] -> Int -> a
elementAt (x:xs) 1 = x
elementAt (x:xs) k = elementAt xs (k - 1)

--4
myLength :: [a] -> Int
myLength [] = 0
myLength (x:xs) = (myLength xs) + 1

--5
myReverse :: [a] -> [a]
myReverse []    = []
myReverse (x:xs)  = (myReverse xs) ++ [x]

myReversef :: [a] -> [a]
myReversef = foldl (flip (:)) []
-- note:
--  flip (:) xs x = x:xs

--6
isPalindrome :: Eq a => [a] -> Bool
isPalindrome xs = (xs == (myReverse xs))

--7
data NestedList a = Elem a | List [NestedList a]
myFlatten :: NestedList a -> [a]
myFlatten (Elem a) = [a]
myFlatten (List []) = []
myFlatten (List (x:xs)) = myFlatten x ++ myFlatten (List xs)

--8
compress :: Eq a => [a] -> [a]
compress [] = []
compress [a] = [a]
compress (x:y:xs) = if (x == y) then (compress (x:xs)) else (x:(compress (y:xs)))

--9
--naive
packHelper :: Eq a => [[a]] -> a -> [[a]]
packHelper [[]] y = [[y]]
packHelper x y = if ((last (last x)) == y)
                    then ((init x) ++ [y:(last x)])
                    else (x ++ [[y]])

pack :: Eq a => [a] -> [[a]]
pack = foldl packHelper [[]]

--using the incredibly apt span
packSpan :: Eq a => [a] -> [[a]]
packSpan [] = []
packSpan l  = x:(packSpan xs)
    where (x,xs) = span (== (head l)) l

--10
encode :: Eq a => [a] -> [(Int, a)]
encode [] = []
encode x = map (\x -> ((length x),(head x))) (pack x)

--11
data ListItem a = Single a | Multiple Int a deriving (Show)

encodeMod :: Eq a => [a] -> [ListItem a]
encodeMod = map (\(n, e) -> if (n == 1)
                                then (Single e)
                                else (Multiple n e)) . encode

--12
decodeModified :: [ListItem a] -> [a]
decodeModified = concatMap decodeHelper
    where
        decodeHelper (Single x)     = [x]
        decodeHelper (Multiple n x) = replicate n x
        
--13
encodeDirect :: Eq a => [a] -> [ListItem a]
encodeDirect [] = []
encodeDirect l = if ((length x) > 1)
                    then (Multiple (length x) (head x)):(encodeDirect xs)
                    else (Single (head x)):(encodeDirect xs)
    where
        (x,xs) = span (== (head l)) l
        
--14
dupli :: [a] -> [a]
dupli = concatMap (\x -> [x,x])

--15
repli :: [a] -> Int -> [a]
repli l n = concatMap (\x -> replicate n x) l

--16
dropEvery :: [a] -> Int -> [a]
dropEvery [] _ = []
dropEvery l  n = (take (n - 1) l) ++ dropEvery (drop n l) n

--17
split :: [a] -> Int -> ([a],[a])
split l n = splitHelper ([],l) n
    where
        splitHelper (x,y)  0     = (x, y)
        splitHelper (x,[]) _     = (x, [])
        splitHelper (x,z@(y:ys)) n = if (n > 0)
                                    then splitHelper (x ++ [y], ys) (n - 1)
                                    else (x, z)
        
--18
slice :: [a] -> Int -> Int -> [a]
slice l 0 k = fst (split l k)
slice l i k = snd (split (fst (split l k)) (i - 1))

--19
rotate :: [a] -> Int -> [a]
rotate l n = y ++ x
    where
        (x, y) = split l (n `mod` (length l))
        
--20
removeAt :: Int -> [a] -> (a,[a])
removeAt i l = (y, (xs ++ ys))
    where
        (xs, (y:ys)) = split l (i-1)
        
--21
insertAt :: a -> [a] -> Int -> [a]
insertAt c l i = x ++ c:y
    where
        (x, y) = split l (i - 1)
        
--22
range :: Int -> Int -> [Int]
range i j = if (i == j)
                then [i]
                else if (j > i)
                        then i:(range (i + 1) j)
                        else reverse (range j i)
                        
--23
rndSelect :: [a] -> Int -> [a]
rndSelect _ 0  = []
rndSelect [] _ = []
rndSelect l n  = if (n < 0)
                    then error "n < 0"
                    else x:(rndSelect xs (n-1))
                        where
                            (x, xs) = removeAt 0 l
                            --replace this 0 with a real random index
                            
--24
diffSelect :: Int -> Int -> [Int]
diffSelect n m = rndSelect [1..m] n

--25
-- rndPermu :: [a] -> [a]
-- rndPermu l = rndSelect l (length l)

--26
powerSetIndices :: Int -> [[Int]]
powerSetIndices 0 = [[]]
powerSetIndices k = [xs ++ [k] | xs <- prevPowerSet] ++ prevPowerSet
    where
        prevPowerSet = powerSetIndices (k - 1)
        
recurseCombs :: Int -> Int -> [[Int]]
recurseCombs _ 0 = [[]]
recurseCombs n 1 = [[x] | x <- [1..n]]
recurseCombs n k = [(x:xs) | x <- [1..(n - k + 1)], xs <- (recurseCombs n (k - 1)), x < (head xs)]

--27
--Group the elements of a set into disjoint subsets (list all possible combinations)
--Give a list of group sizes, get a list of partitions
--Different groups of the same size are considered distinct

--28
--Sort a list of lists according to list length

mergeSort :: (Ord a) => [a] -> [a]
mergeSort []     = []
mergeSort [x]      = [x]
mergeSort l = mergeHelper (mergeSort first) (mergeSort second)
    where
        (first, second) = split l ((length l) `div` 2)

--helper function: interpolate two sorted lists (test)
mergeHelper :: (Ord a) => [a] -> [a] -> [a]
mergeHelper [] x = x
mergeHelper x [] = x
mergeHelper (x:xs) (y:ys) = if (x <= y) then (x:(mergeHelper xs (y:ys))) else (y:(mergeHelper (x:xs) ys))

--helper function for two lists of lists sorted by length of element
lmerge :: [[a]] -> [[a]] -> [[a]]
lmerge [] x = x
lmerge x [] = x
lmerge (x:xs) (y:ys) = if ((length x) <= (length y)) then (x:(lmerge xs (y:ys))) else (y:(lmerge (x:xs) ys))

lMergeSort :: [[a]] -> [[a]]
lMergeSort [[]]     = [[]]
lMergeSort [x]      = [x]
lMergeSort l = lmerge (lMergeSort first) (lMergeSort second)
    where
        (first, second) = split l ((length l) `div` 2)

--b. by frequency of length (least common, second least common, etc)
lengthAccum :: [[[a]]] -> [a] -> [[[a]]]
lengthAccum (x:xs) y  = if ((length (head x)) == (length y))
                    then ((y:x):xs)
                    else ([y]:(x:xs))
                    
groupByLength :: [[a]] -> [[a]]
groupByLength [] = []
groupByLength l = foldl (++) [] (lMergeSort (foldl lengthAccum [[x]] xs))
    where
        (x:xs) = lMergeSort l
        
--31
--Determine whether a given integer number is prime.
isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime k = not (any (\x -> ((mod k x) == 0)) [x | x <- [2..k], x^2 <= k])

--uses sieve
isPrime' :: Int -> Bool
isPrime' 2 = True
isPrime' n = all (/=0) [n `mod` q | q <- takeWhile (<= (ceiling . sqrt . fromIntegral) n) primeSieve]

--32
--Determine the greatest common divisor of two positive integer numbers.
myGCD :: Int -> Int -> Int
myGCD a 0 = a
myGCD a b = myGCD b (a `mod` b)

--33
--Determine whether two positive integer numbers are coprime.
coprime :: Int -> Int -> Bool
coprime a b = ((myGCD a b) == 1)

--34
--Calculate Euler's totient function phi(m). Euler's so-called totient function phi(m) is defined as the number of positive integers r (1 <= r < m) that are coprime to m.
countTrue :: [Bool] -> Int
countTrue = foldl (\acc x -> if x then (acc + 1) else acc) 0

totient :: Int -> Int
totient n = countTrue (map (\x -> (coprime x n)) [1..(n-1)])

--35
--Determine the prime factors of a given positive integer. Construct a flat list containing the prime factors in ascending order.
primeFactorsList :: Int -> [Int]
primeFactorsList n = [x | x <- [2..n], isPrime x, (mod n x) == 0]

primeFactorsList' :: Int -> [Int]
primeFactorsList' 1 = []
primeFactorsList' n = if isPrime' n
                        then [n]
                        else q:(primeFactorsList' (n `div` q))
                            where
                                q = head [x | x <- takeWhile (<= n) primeSieve, (mod n x) == 0]

--naive and slow (refactors the number)
primeFactors :: Int -> [Int]
primeFactors 1 = []
primeFactors n = mergeSort ((primeFactorsList n) ++ primeFactors (foldl div n (primeFactorsList n)))

-- factorReduce n r returns (q, p), where p is the exponent of a factor (or non-factor) r of n, and q is n/(r^p)
factorReduce :: Int -> Int -> (Int, Int, Int)
factorReduce n r = if ((mod n r) /= 0)
                    then (n, r, 0)
                    else (m, r, 1 + i)
                        where
                            (m, _, i) = factorReduce (div n r) r

--Less naive?
primeFactors2 :: Int -> [Int]
primeFactors2 1 = []
primeFactors2 n = foldl (++) [] [replicate p r | (_, r, p) <- [factorReduce n r | r <- flist]]
    where
        flist = primeFactorsList n

--minus A B yields the set difference (A - B) := [a | a <- A, a not in B], where sets are represented as ordered lists
minus :: (Ord a) => [a] -> [a] -> [a]
minus (x:xs) (y:ys) = case (compare x y) of
    LT -> x:(minus xs (y:ys))
    EQ -> minus xs ys
    GT -> minus (x:xs) ys
minus a _ = a

--union A B yields the set union (A + B)
union :: (Ord a) => [a] -> [a] -> [a]
union (x:xs) (y:ys) = case (compare x y) of
    LT -> x:(union xs (y:ys))
    EQ -> x:(union xs ys)
    GT -> y:(union (x:xs) ys)
union a [] = a
union [] b = b

--generalized union of two ordered sets (using custom comparison)
unionBy :: (a -> a -> Ordering) -> [a] -> [a] -> [a]
unionBy _ a [] = a
unionBy _ [] b = b
unionBy comparison (x:xs) (y:ys) = case (comparison x y) of
    LT -> x:(unionBy comparison xs (y:ys))
    EQ -> x:(unionBy comparison xs ys)
    GT -> y:(unionBy comparison (x:xs) ys)    
    
mergeSortLL :: (Ord a) => [[a]] -> [[a]]
mergeSortLL []     = []
mergeSortLL [x]      = [x]
mergeSortLL l = mergeHelperLL (mergeSortLL first) (mergeSortLL second)
    where
        (first, second) = split l ((length l) `div` 2)

--helper function: interpolate two sorted lists 
mergeHelperLL :: (Ord a) => [[a]] -> [[a]] -> [[a]]
mergeHelperLL [] x = x
mergeHelperLL x [] = x
mergeHelperLL (x:xs) (y:ys) = if ((head x) <= (head y))
                            then (x:(mergeHelperLL xs (y:ys)))
                            else (y:(mergeHelperLL (x:xs) ys))
        
--assumes that lists are ordered representations of sets and that the heads of the lists are ordered
unionAll :: (Ord a) => [[a]] -> [a]
unionAll [[]] = []
unionAll l = x:(unionAll (mergeHelperLL (mergeSortLL [tail xs | xs <- lfirst, xs /= []]) lsecond))
    where
        x = head (head l)
        (lfirst,lsecond) = span ((== x) . head) l

primeSieve :: [Int]
primeSieve = 2:3:(minus [5,7..] (unionAll [[p*p,p*p+p*2..] | p <- (tail primeSieve)]))

validateSieve  = map (any (==0)) [map (mod p) (takeWhile (< (ceiling . sqrt . fromIntegral) p) primeSieve) | p <- primeSieve]
validateSieve2 = map (any (==0)) [map (mod p) (takeWhile (< (ceiling . sqrt . fromIntegral) p) [2..]) | p <- primeSieve]

findTwinPrimes = (2,3):[(p, p + 2) | p <- primeSieve, isPrime' (p + 2)]
findTriplePrimes = [(p, if (isPrime' (p+2)) then p+2 else p+4, p+6) | p <- primeSieve, isPrime' (p+6), (isPrime' (p+2) || isPrime' (p+4))]