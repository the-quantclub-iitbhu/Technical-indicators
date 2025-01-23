def calculate_atr(data, window=14):
    """
    Calculate the Average True Range (ATR).

    ATR is a measure of market volatility.

    Parameters:
    ----------
    data : pandas.DataFrame
        A DataFrame containing at least the 'high', 'low', and 'close' columns.
    window : int, optional
        The rolling window period for calculating the ATR. Default is 14.

    Returns:
    -------
    atr : pandas.Series
        The Average True Range values.
    """
    tr1 = data['high'] - data['low']
    tr2 = abs(data['high'] - data['close'].shift(1))
    tr3 = abs(data['low'] - data['close'].shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.rolling(window).mean()
    return atr
