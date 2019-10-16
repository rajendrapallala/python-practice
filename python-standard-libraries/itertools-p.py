from itertools import groupby
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
if __name__ == "__main__":
    s = '1222311'
    l = [(k, list(g)) for k,g in groupby(s)]
    print(l)