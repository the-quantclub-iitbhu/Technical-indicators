def calculate_ema(data, column, period):
    """
    Calculates the Exponential Moving Average (EMA) for a specified column.

    EMA is a weighted moving average that reacts more significantly to recent price changes.

    Parameters:
    ----------
    data : pd.DataFrame
        The input DataFrame containing the data.
    column : str
        The column name on which the EMA will be calculated.
    period : int
        The lookback period for the EMA.

    Returns:
    -------
    pd.Series
        A Series containing the EMA values.

    Example Usage:
    --------------
    ```python
    data['EMA_20'] = calculate_ema(data, 'close', period=20)
    ```
    """
    return data[column].ewm(span=period, adjust=False).mean()
