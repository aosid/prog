import Data.List

and' :: Bool -> Bool -> Bool
and' True True = True
and' _    _    = False

or' :: Bool -> Bool -> Bool
or' False False = False
or' _     _     = True

not' :: Bool -> Bool
not' True = False
not' False = True

nor' :: Bool -> Bool -> Bool
nor' False False = True
nor' _     _     = False

nand' :: Bool -> Bool -> Bool
nand' True True = False
nand' _    _    = True

xor' :: Bool -> Bool -> Bool
xor' x y = not' (x `equ'` y)

impl' :: Bool -> Bool -> Bool
impl' True False = False
impl' _    _     = True

equ' :: Bool -> Bool -> Bool
equ' True True   = True
equ' False False = True
equ' _     _     = False

-- Print truth table for binary boolean function
table' :: (Bool -> Bool -> Bool) -> String
table' f = printBinary f [True, False]

printBinary :: (Show a) => (a -> a -> a) -> [a] -> String
printBinary f domain = concatMap (++ "\n") [printBinaryInstance f x y | x <- domain, y <- domain]

printBinaryInstance :: (Show a) => (a -> a -> a) -> a -> a -> String
printBinaryInstance f x y = show x ++ " " ++ show y ++ " " ++ show (f x y)

-- Print truth table for boolean function of arbitrary number of variables (arguments to function given as a list of length n)
tablen :: Int -> ([Bool] -> Bool) -> String
tablen n f = concatMap (++ "\n") [printGeneralInstance f x | x <- enumerateDomain n [True, False]]

printGeneralInstance :: (Show a) => ([a] -> a) -> [a] -> String
printGeneralInstance f l = (concatMap (\x -> (show x) ++ "\t") l) ++ (show (f l))

enumerateDomain :: Int -> [a] -> [[a]]
enumerateDomain 1 l = [[x] | x <- l]
enumerateDomain n l = [(x:subl) | x <- l, subl <- enumerateDomain (n - 1) l]

gray :: Integral a => a -> [String]
gray 0 = [""]
gray n = foldr (\s acc -> ("0" ++ s):acc++["1" ++ s]) [] $ gray (n-1)

-- Huffman encoding!!
data HTree a = Leaf a | Branch (HTree a) (HTree a)
    deriving Show
    
insertOn :: Ord b => (a -> b) -> a -> [a] -> [a]
insertOn f x ys = insertBy (\x y -> compare (f x) (f y)) x ys

huffman :: (Ord a, Num a) => [(Char, a)] -> [(Char, String)]
huffman [] = []
huffman l = parseTree ((huffHelp $ sortOn huffWeight [Leaf x | x <- l]) !! 0)
    where
        huffWeight (Leaf x)       = snd x
        huffWeight (Branch x y) = (huffWeight x) + (huffWeight y)

        huffHelp (x:[]) = [x]
        huffHelp (x:y:xs) = huffHelp (insertOn huffWeight (Branch x y) xs)

        parseTree (Leaf (x, _)) = [(x, "")]
        parseTree (Branch xs ys) = sortOn fst [(x, '0':path) | (x, path) <- parseTree xs] ++ [(y, '1':path) | (y, path) <- parseTree ys]