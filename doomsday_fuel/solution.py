from fractions import gcd
from fractions import Fraction as f


def compute_probabilies(m):
    res = [f(0, 1)]
    for i, row in enumerate(m):
        if sum(row) == 0:
            # It is a terminal state
            continue

        res = [f(0, 1)] * len(row)
        last = []
        for j, element in enumerate(row):
            if j <= i:
                continue
            # Magic P = P(next|accumulated) + P(other_path|accumulated)
            # Lets go step by step

            # Probability of getting to this row = P(past)
            p_past = m[i-1][i] if i > 0 else 1

            # Probability to get to next row without passing by this row
            # P(other_path)
            p_other_path = m[i-1][j] if i > 0 else 0

            # P(next) = element value / total of row
            p_next = f(element, sum(row))

            # P(accumulated) = summation(P(next)*P(past))**n
            # https://es.wikipedia.org/wiki/Anexo:Series_matem%C3%A1ticas
            # P(accumulated) = 1 / (1 - P(next)*P(past))
            p_accumulated = 1 / (1 - p_past*row[0]/sum(row))

            # And we are ready
            p = (p_next * p_past + p_other_path) * p_accumulated
            res[j] = p

        m[i] = res
        res = res[i+1:]
    return res


def answer(m):
    probabilities = compute_probabilies(m)
    denominator = reduce(gcd, probabilities)
    return [
        (p / denominator).numerator for p in probabilities
    ] + [denominator.denominator]

m = [
   [0, 1, 0, 0, 0, 1],
   [4, 0, 0, 3, 2, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0],
 ]
assert answer(m) == [0, 3, 2, 9, 14]


m = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

assert answer(m) == [7, 6, 8, 21]
