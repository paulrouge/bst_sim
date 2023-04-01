import config
import random

# getters
def one_percent_chance():
    return random.randint(0,100) < 1

def five_percent_chance():
    return random.randint(0,100) < 5

def getBstSupply():
    return config.TOTAL_SUPPLY

def getBnUsdInContract():
    return config.BNUSD_IN_CONTRACT

def getBstPrice():
    if config.BNUSD_IN_CONTRACT == 0 or config.TOTAL_SUPPLY == 0:
        return config.INIT_PRICE
    return config.BNUSD_IN_CONTRACT / config.TOTAL_SUPPLY

# returns a random amount to substract from total supply, 
# between 0 and 10% of total supply and a 0.3% chance of 6% of total supply
def getRedeemAmount():
    price = config.BNUSD_IN_CONTRACT / config.TOTAL_SUPPLY
    
    if five_percent_chance():
        return config.TOTAL_SUPPLY * 0.03
    if five_percent_chance():
        return config.TOTAL_SUPPLY * 0.01
    else:
        # the higher the price, the lower the max amount
        max_amount = config.TOTAL_SUPPLY * 0.01 * (1 / price)
        return random.randint(0, int(max_amount))