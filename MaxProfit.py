def solution(A):
    max_profit = 0
    min_price = 200000
    for price in A:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price-min_price)

    return max_profit
