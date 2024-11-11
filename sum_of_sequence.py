def sequence(n):
    s_n = 0
    for i in range(1, n+1):
        s_n = s_n + i/(1+1)
    return s_n

print(sequence(3))