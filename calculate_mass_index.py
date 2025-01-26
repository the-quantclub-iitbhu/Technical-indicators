def mass_index(data, period=9, ema_period=25):
    """
    Calculates the Mass Index for a given DataFrame.

    The Mass Index uses the range between high and low prices to detect trend reversals.

    Parameters:
    ----------
    data : pd.DataFrame
        A DataFrame containing 'ha_high' and 'ha_low' columns (Heikin-Ashi high/low).
    period : int, optional
        The period for calculating the exponential moving averages (EMA). Default is 9.
    ema_period : int, optional
        The period for calculating the rolling sum of EMA ratios. Default is 25.

    Returns:
    -------
    pd.Series
        A series representing the Mass Index values.

    Example Usage:
    --------------
    ```python
    data['Mass_Index'] = mass_index(data, period=9, ema_period=25)
    ```
    """
    high_low_diff = data['ha_high'] - data['ha_low']

    # Calculate EMA1
    ema1 = high_low_diff.ewm(span=period, adjust=False).mean()

    # Calculate EMA2
    ema2 = ema1.ewm(span=period, adjust=False).mean()

    # Calculate EMA ratio
    ema_ratio = ema1 / ema2

    # Calculate Mass Index
    mass_index = ema_ratio.rolling(window=ema_period).sum()

    return mass_index
