import pandas_ta as ta
def kairi_relative_index(df, length=14):
    """
    Calculates the Kairi Relative Index (KRI) for a given DataFrame.

    The KRI measures the percentage deviation of the current price from its moving average (SMA).
    It is useful in identifying overbought or oversold market conditions.

    Parameters:
    ----------
    df : pd.DataFrame
        A DataFrame containing the 'ha_close' (Heikin-Ashi close) column.
    length : int, optional
        The lookback period for calculating the SMA. Default is 14.

    Returns:
    -------
    pd.Series
        A series representing the KRI values.

    Example Usage:
    --------------
    ```python
    df['KRI'] = kairi_relative_index(df, length=14)
    ```
    """
    # Calculate the moving average (SMA)
    df['sma'] = ta.sma(df['ha_close'], length)

    # Calculate the KRI
    df['kri'] = ((df['ha_close'] - df['sma']) / df['sma']) * 100

    return df['kri']
