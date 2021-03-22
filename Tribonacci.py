def tribonacci(x):
    a = 0
    b = 1
    c = 2
    print(f"{a}\n{b}\n{c}")
    for i in range(3, x):
        d = a + b + c
        print(d)
        a = b
        b = c
        c = d


tribonacci(1)
