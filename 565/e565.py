import math

def divisors(n):
    results = [1, n]
    upper_bound = int(n ** 0.5)
    for i in range(1, upper_bound):
        i += 1
        if n % i == 0:
            results.extend([i, n / i])
    results =  list(set(results))
    results.sort()
    results = tuple(results)
    return results

def sum_of_divisors(n):
    return sum(divisors(n))

def divisible_sum_of_divisors(n, d):
    divisible_sums = []
    for i in range(0, n):
        i += 1
        if sum_of_divisors(i) % d == 0:
            divisible_sums.append(i)
    print divisible_sums
    results = sum(divisible_sums)
    return results
    


if __name__ == "__main__":
    pass
