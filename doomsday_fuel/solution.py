from fractions import gcd
from fractions import Fraction as f


def compute_probabilies(m):
    res = [f(0, 1)]
    terminal_states = []
    for i, row in enumerate(m):
        if sum(row) == 0:
            # It is a terminal state
            terminal_states.append(i)
            continue

        res = [f(0, 1)] * len(row)
        total = sum(row)
        p_past = []
        for j, element in enumerate(row):
            last = 0
            # Magic P = P(next|paths)
            # Lets go step by step
            element = f(element, total)
            if i == 0:
                res[j] = element
                continue

            if j < i and m[j][i]:
                # Probability of getting to this row = P(past)

                # P(accumulated) = summation(P(next)*P(past))**n
                # https://es.wikipedia.org/wiki/Anexo:Series_matem%C3%A1ticas
                # P(accumulated) = 1 / (1 - P(next)*P(past))
                last = f(
                    m[j][i].numerator,
                    m[j][i].denominator - len(p_past)
                )
                p_past.append(last / (1 - element * last))

            print('p_past {}:'.format(p_past))

            last = 0
            # And we are ready
            if m[i-1][j]:
                last = f(
                    m[i-1][j].numerator,
                    m[i-1][j].denominator - len(p_past)
                )

            p = (element + last) * sum(p_past)
            res[j] = p

        print('partial res {}: '.format(res))
        m[i] = res
    print(terminal_states)
    return [e for i, e in enumerate(res) if i in terminal_states]


def answer(m):
    probabilities = compute_probabilies(m)
    print(probabilities)
    denominator = reduce(gcd, probabilities)
    print(denominator)
    return [
        (p / denominator).numerator for p in probabilities
    ] + [denominator.denominator]


print(1)
m = [
   [0, 1, 0, 0, 0, 1],
   [4, 0, 0, 3, 2, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0],
 ]
res = answer(m)
assert res == [0, 3, 2, 9, 14], res

print(2)
m = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
res = answer(m)

assert res == [7, 6, 8, 21], res

print(3)
m = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 3, 0, 0]
]

res = answer(m)
assert res == ['donnu'], res
