def pas(n):
    if n == 1:
        return [1]
    else:
        return [1] + [(pas(n-1)[i])+(pas(n-1)[i+1]) for i in range(n-2)] + [1]


print(pas(8))  # [1, 7, 21, 35, 35, 21, 7, 1]
