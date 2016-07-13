def fibr(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibi(n):
    if n==0 or n==1:
        return n
    grandparent = 0
    parent = 1
    for i in range(2, n+1):
        current = grandparent + parent
        grandparent = parent
        parent = current
    return current

def sum_even_fibs_under(n):
    stop = 0
    i = 1
    fibs = []
    while stop==0:
        i += 1
        if fibi(i) % 2 == 0:
            fibs.append(fibi(i))
        if fibi(i) > n:
            stop = 1
    print fibs
    return sum(fibs)
        
