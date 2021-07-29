def sieve(n : int):

    prime = [True for i in range(n - 1)]
    p = 2
    #
    # why p*p because af factors are been repeated
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p, n + 1, p)
                prime[i] = False
        p += 1

    for p in range(2, n + 1):
        if prime[p] == True:
            print(p, end=" ")
