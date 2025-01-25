def hma(src, period):
    """
    Calculates the Hull Moving Average (HMA) for a given data series.

    The HMA is a weighted moving average that reduces lag while improving the smoothing. 
    It is commonly used in technical analysis for identifying trends.

    Parameters:
    ----------
    src : pd.Series
        The source data (e.g., closing prices).
    period : int
        The lookback period for the HMA.

    Returns:
    -------
    pd.Series
        A series representing the HMA values.

    Example Usage:
    --------------
    ```python
    hma_result = hma(data['close'], period=14)
    ```
    """
    wma1 = src.rolling(int(period / 2)).mean() * 2
    wma2 = src.rolling(period).mean()
    diff = wma1 - wma2
    return diff.rolling(int(period**0.5)).mean()
