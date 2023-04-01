import config



# USD in, BST out
def redeemBnusd(_amountOfBstTokens):

    _price = config.BNUSD_IN_CONTRACT / config.TOTAL_SUPPLY
    _bnusd_value = _amountOfBstTokens * _price

    while _bnusd_value > config.CHUNK_SIZE:
        _bst_amount = config.CHUNK_SIZE / _price
        _post_fee = _bst_amount * config.FEE
        config.TOTAL_SUPPLY -= _bst_amount

        _value_post_fee = _post_fee * _price
        config.BNUSD_IN_CONTRACT -= _value_post_fee

        # update price
        _price = config.BNUSD_IN_CONTRACT / config.TOTAL_SUPPLY

        # update amount
        _bnusd_value -= _value_post_fee

        # update amount of tokens
        _amountOfBstTokens -= _bst_amount

    # get remainder
    if _amountOfBstTokens > 0:
        _post_fee = _amountOfBstTokens * config.FEE
        config.TOTAL_SUPPLY -= _amountOfBstTokens

        _value_post_fee = _post_fee * _price
        config.BNUSD_IN_CONTRACT -= _value_post_fee