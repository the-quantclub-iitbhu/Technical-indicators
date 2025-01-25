def thma(src_col, period):
    """
    Calculates the Triple Hull Moving Average (THMA) for a given data series.

    The THMA applies the HMA calculation three times to achieve greater smoothness and 
    responsiveness, which makes it effective for identifying trends and momentum shifts.

    Parameters:
    ----------
    src_col : pd.Series
        The source data (e.g., closing prices).
    period : int
        The lookback period for the THMA.

    Returns:
    -------
    pd.Series
        A series representing the THMA values.

    Example Usage:
    --------------
    ```python
    thma_result = thma(data['close'], period=14)
    ```
    """
    ma1 = hma(src_col, period)
    ma2 = hma(ma1, period)
    ma3 = hma(ma2, period)
    return 3 * (ma1 - ma2) + ma3
