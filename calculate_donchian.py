def calculate_donchian(data, period):
    """
    Calculates the Donchian Channel midline for a given DataFrame.

    The Donchian Channel is calculated as the average of the highest high and lowest low over the lookback period.

    Parameters:
    ----------
    data : pd.DataFrame
        A DataFrame containing 'high' and 'low' columns.
    period : int
        The lookback period for the Donchian Channel.

    Returns:
    -------
    pd.Series
        A Series representing the Donchian Channel midline values.

    Example Usage:
    --------------
    ```python
    data['Donchian_Channel'] = donchian(data, period=20)
    ```
    """
    return (data['low'].rolling(window=period).min() + data['high'].rolling(window=period).max()) / 2
