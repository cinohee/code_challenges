from fractions import gcd
from fractions import Fraction as f


def compute_probabilies(m):
    res = [f(0, 1)] * len(m)
    terminal_states = []
    for i, row in enumerate(m):
        if sum(row) == 0:
            # It is a terminal state
            terminal_states.append(i)
            continue

        total = sum(row)
        p_past = []
        for j, element in enumerate(row):
            res[j] = f(element, total)
            if i == 0:
                continue

            if j < i and m[j][i]:
                p_past.append(f(m[j][i], (1 - res[j] * m[j][i])))
                continue

            last = 0
            ii = 0
            while ii < i:
                last += f(m[ii][j], (1 - (res[ii] * m[ii][ii + 1])))
                ii += 1

            res[j] = (res[j] * sum(p_past)) + last

        print('partial res {}: '.format(res[:]))
        m[i] = res[:]

    print(terminal_states)
    return [e for i, e in enumerate(res) if i in terminal_states]


def answer(m):
    probabilities = compute_probabilies(m)
    print(probabilities)
    denominator = reduce(gcd, probabilities)
    print(denominator)
    return [
        (f(p, denominator)).numerator for p in probabilities
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
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 3, 1, 0]
]

res = answer(m)
assert res == [1, 1], res

print(4444)
m = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

res = answer(m)
assert res == [1, 100], res
