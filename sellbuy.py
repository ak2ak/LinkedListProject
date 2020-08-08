# def sell_buy(A):
#     smallest = A[0]
#     max_profit = 0
#     for i in A:
#         if smallest > i:
#             smallest = i
#         max_profit = max(max_profit, i - smallest)
#     return max_profit
#
#
# print(sell_buy([310, 315, 240, 250, 260, 310]))
def mini(q):
    counter = 0
    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0,q[i]-2),i):
            if q[j]>q[i]:
                counter+=1
    print(counter)

mini([2,1,5,3,4])