def calculate_bbp(data, bbp_length=50):
    """
    Calculates the Bullish-Bearish Power (BBP) indicator for a given DataFrame.

    The BBP indicator combines the BullPower and BearPower indicators to measure the 
    strength of a trend by comparing the current price with the Exponential Moving Average (EMA) 
    over a specified period.

    Parameters:
    data (pd.DataFrame): DataFrame with 'close', 'high', and 'low' columns representing the price data.
    bbp_length (int): The length of the EMA window. Default is 50.

    Returns:
    pd.DataFrame: The original DataFrame with added columns:
                  - 'BullPower': The difference between the high price and the EMA.
                  - 'BearPower': The difference between the low price and the EMA.
                  - 'BBP': The sum of BullPower and BearPower, representing the overall power.
    """
    # Calculate the Exponential Moving Average (EMA)
    ema = data['close'].ewm(span=bbp_length, adjust=False).mean()
    
    # Calculate BullPower and BearPower
    data['BullPower'] = data['high'] - ema
    data['BearPower'] = data['low'] - ema
    
    # Calculate BBP
    data['BBP'] = data['BullPower'] + data['BearPower']
    
    return data
