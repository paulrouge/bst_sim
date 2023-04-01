from config import CHUNK_SIZE, FEE, INIT_PRICE
import config

# amount is in bnusd
def mintBst(amount):
    _mint_no_tax = 0

    if config.TOTAL_SUPPLY == 0:
        _mint_no_tax = amount / INIT_PRICE
        config.TOTAL_SUPPLY += _mint_no_tax
        config.BNUSD_IN_CONTRACT += amount
    else:
        _mint_no_tax = config.TOTAL_SUPPLY * amount / INIT_PRICE
    
    # get number of 500 chunks
    num_of_chunks = int(amount / CHUNK_SIZE)

    for i in range(num_of_chunks):
        _mint_no_tax = config.TOTAL_SUPPLY * CHUNK_SIZE / config.BNUSD_IN_CONTRACT
        config.TOTAL_SUPPLY += _mint_no_tax * FEE
        config.BNUSD_IN_CONTRACT += CHUNK_SIZE

    # get remainder
    remainder = amount % CHUNK_SIZE

    if remainder != 0:
        _mint_no_tax = config.TOTAL_SUPPLY * remainder / config.BNUSD_IN_CONTRACT
        config.TOTAL_SUPPLY += _mint_no_tax * FEE
        config.BNUSD_IN_CONTRACT += remainder