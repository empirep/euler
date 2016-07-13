def is_factor(n, factor):
    return n % factor == 0

def multiples_below(n, factors):
    if not isinstance(factors, list):
        print 'Argument factors must be a list'
        return

    results = []

    for test in range(1, n):
        for factor in factors:
            if test % factor == 0:
                results.append(test)

    return results

def sum_multiples_below(n, factors):
    if not isinstance(factors, list):
        print 'Argument factors must be a list'
        return

    return sum(multiples_below(n, factors))
