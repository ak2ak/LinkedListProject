def fibonacci(l, memo={}):
    if l<=1:
        return 1
    try:
        return memo[l]
    except:
        result = fibonacci(l-1,memo)+fibonacci(l-2,memo)
        memo[l]=result
        return memo[l]

print(fibonacci(4))