def get_fibo(n1=0, n2=1):
    yield n1
    while n2 < 10000:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        yield n1


v = get_fibo()
for i in range(100):
    print(next(v))