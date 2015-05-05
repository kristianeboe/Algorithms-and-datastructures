from sys import stdin

def minCoinsGreedy(coins, value):
    counter = 0
    print (coins)
    for coin in coins:
        amount = value//coin
        #if amount > 0:
        #    print (amount)
        value = value % coin
        if amount > 0:
            counter += amount
        if value == 0:
            return counter

    # SKRIV DIN KODE HER

def minCoinsDynamic(coins, value):
    # SKRIV DIN KODE HER
    return 0
def canUseGreedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    return 0

Inf = 1000000000
coins = [1000, 20, 500, 1, 100, 50, 5, 10, 200, 4]
# for c in stdin.readline().split():
#     coins.append(int(c))
coins.sort()
coins.reverse()
# method = stdin.readline().strip()
# if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
#     for line in stdin:
#         print minCoinsGreedy(coins, int(line))
# else:
#     for line in stdin:
#         print minCoinsDynamic(coins, int(line))

print (minCoinsGreedy(coins, 1024))
