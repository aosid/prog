import Data.List

data Card = Card Int Suit
    deriving (Show, Eq, Ord)
data Suit = SPADES | HEARTS | CLUBS | DIAMONDS
    deriving (Show, Eq, Ord)

v = Card 10 CLUBS    
w = Card 11 SPADES
x = Card 1 SPADES
y = Card 2 SPADES
z = Card 5 SPADES

hand = [v,w,x,y,z]
    
rank :: Card -> Int
rank (Card x _) = x

suit :: Card -> Suit
suit (Card _ x) = x

-- countHand isCrib (flipcard:hand) = the score of hand
countHand :: Bool -> [Card] -> Int
countHand isCrib hand@(flip:held) = flushscore + sum (map (\f -> f hand) [fifteen, pair, runs, knobs])
    where
        flushscore = if isCrib
                        then flush hand
                        else if (suit flip) == (suit (head held))
                            then flush hand
                            else flush held

subHands :: [Card] -> [[Card]]
subHands [] = [[]]
subHands (x:xs) = [(x:y) | y <- subHands xs] ++ (subHands xs)

sumHand :: [Card] -> Int
sumHand [] = 0
sumHand (x:xs) = if (rank x) > 10
                    then 10   + (sumHand xs)
                    else (rank x) + (sumHand xs)                           
        
fifteen :: [Card] -> Int
fifteen [] = 0
fifteen ls = sum $ map (\x -> if (sumHand x == 15) then 2 else 0) (subHands ls)

pair :: [Card] -> Int
pair [] = 0
pair (x:xs) = (sum $ map (\y -> if (rank y) == (rank x) then 2 else 0) xs) + (pair xs)

-- this returns true if the input hand is a run (cards of sequential rank with no repeats)
isRun :: [Card] -> Bool
isRun ls = isRunHelper (sortOn rank ls)
    where
        isRunHelper (x:y:xs) = if abs ((rank x) - (rank y)) == 1
                                    then True && (isRunHelper (y:xs))
                                    else False
        isRunHelper _ = True
        
-- examines subhands, counts scores for runs of maximal length (all maximal runs in a hand are of the same length)
runs :: [Card] -> Int
runs ls = runHelper (subHands ls) (length ls)
    where
        runHelper l n = if (runSum > 0)
                            then runSum
                            else if (n > 3)
                                    then (runHelper l (n - 1))
                                    else 0
            where
                runSum = sum (map (\x -> if (isRun x) then n else 0) (filter (\x -> length x == n) l))

-- because cribbage is crazy, the matter of the cut card and flushes in the crib are handled outside this function.
flush :: [Card] -> Int
flush [] = 0
flush hand@(x:xs) = if all (\y -> (suit y) == (suit x)) xs then length hand else 0

-- the first element is the cut card.
knobs :: [Card] -> Int
knobs [] = 0
knobs (x:xs) = if any (== (Card 11 (suit x))) xs then 1 else 0