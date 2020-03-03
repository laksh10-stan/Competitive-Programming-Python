for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    l1 = sorted(l)
    l2 = [0]*m
    a, c, d, b = 0, 0, 10**9, 0
    for i in range(n):
        if l1[i] == c:
            b = l[b+1:n].index(l1[i]) + b + 1
        else:
            b = l.index(l1[i])
            c = l1[i]
        if a != m:
            a += 1
            l2[b%m] = l1[i]
            if a == m:
                d = l1[i] - min(l2)
        else:
            l2[b%m] = l1[i]
            e = l1[i] - min(l2)
            if d > e:
                d = e
    print(d)