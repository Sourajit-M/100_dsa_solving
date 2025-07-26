def best_time_to_buy_and_sell_stocks(prices):
    buy = 0
    sell = buy+1
    max_profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
        else:
            buy = sell
        sell += 1

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
if __name__ == "__main__":
    print(best_time_to_buy_and_sell_stocks(prices))