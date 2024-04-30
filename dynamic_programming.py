import math

def change(amount, coins):
    """
    Calculates the minimum number of coins needed to make up the given amount.

    Parameters:
    amount (int): The total amount for which change is needed.
    coins (list): A list of coin denominations available.

    Returns:
    int: The minimum number of coins needed to make the amount, or math.inf if it is not possible.
    """
    dp = [math.inf] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
    return dp[amount] if dp[amount] != math.inf else math.inf

def giveChange(amount, coins):
    """
    Determines the minimum number of coins and the specific coins needed to make up the given amount.

    Parameters:
    amount (int): The total amount for which change is needed.
    coins (list): A list of coin denominations available.

    Returns:
    list: A list containing the minimum number of coins and a list of the coins used.
    """
    dp = [math.inf] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == math.inf:
        return [math.inf, []]

    result_coins = []
    current_amount = amount
    while current_amount > 0:
        if coin_used[current_amount] == 0:
            return [math.inf, []]
        result_coins.append(coin_used[current_amount])
        current_amount -= coin_used[current_amount]

    return [len(result_coins), result_coins]

if __name__ == "__main__":
    # Example test cases
    print(change(48, [1, 5, 10, 25, 50]))  # Output: 6
    print(giveChange(48, [1, 5, 10, 25, 50]))  # Output: [6, [25, 10, 10, 1, 1, 1]]

    print(giveChange(48, [1, 7, 24, 42]))  # Output: [2, [24, 24]]
    print(giveChange(35, [1, 3, 16, 30, 50]))  # Output: [3, [16, 16, 3]]
    print(giveChange(6, [4, 5, 9]))  # Output: [math.inf, []]
