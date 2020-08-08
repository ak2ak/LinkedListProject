def bubble_sort(s: list):
    n = len(s)
    for i in range(n):
        for j in range(n - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s


ls = bubble_sort([64, 35, 25, 12, 22, 11, 90])
print(ls)