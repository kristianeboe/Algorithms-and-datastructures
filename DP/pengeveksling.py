from sys import stdin

def minCoinsGreedy(coins, value):
    number_of_coins = 0
    for coin in coins:
        number_of_coins += value//coin
        value = value%coin
    return number_of_coins

def minCoinsDynamic(coins, value):
    dp_coins = [Inf]*(value+1)
    dp_coins[0] = 0
    dp_coins[1] = 1
    for i in range(2,value+1):
        for coin in coins:
            if coin <= i:
                dp_coins[i] = min(dp_coins[i-coin]+1, dp_coins[i])
    return dp_coins[-1]

def canUseGreedy(coins):
    for i in range(len(coins)-1):
        if coins[i]%coins[i+1] != 0:
            return False
    return True

Inf = 1000000000
coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
    for line in stdin:
        print minCoinsGreedy(coins, int(line))
else:
    for line in stdin:
        print minCoinsDynamic(coins, int(line))
