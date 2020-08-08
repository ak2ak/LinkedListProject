def two_sum_hash_map(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]],A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False


two_sum_hash_map([1, 3, 5, 3, 6], 9)
