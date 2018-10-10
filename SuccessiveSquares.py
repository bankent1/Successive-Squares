"""
Travis Banken
Successive Squares
"""
### WORKING :) ###

binExp = []

# evaluates expression using successive squares
def successiveSquares(a, b, n):
    prod = 1
    binRep = "{0:b}".format(b)[::-1]
    print(binRep)
    prev = a % n
    for c in binRep:
        if c == '1':
            #print(prev)
            prod = (prod * prev) % n
        prev = prev**2 % n
    return prod


def main():
    print("This program evaluates the expression a^b(mod n) using successive squares")
    a = int (input("Enter a: "))
    b = int (input("Enter b: "))
    n = int (input("Enter n: "))
    print(f'Evaluating {a}^{b} (mod {n})...')
    ans = successiveSquares(a, b, n)
    print(f'Answer = {ans}')
    print("DONE")

main()
