def calculate_percentage_oscillator(data, short_length=10, long_length=21, source_col='close'):
    """
    Calculates the Percentage Oscillator (PO) for a given DataFrame.

    The PO measures the percentage difference between a short-term and a long-term 
    exponential moving average (EMA). It is often used to identify momentum changes.

    Parameters:
    ----------
    data : pd.DataFrame
        A DataFrame containing the source column (e.g., closing prices).
    short_length : int, optional
        The period for the short EMA. Default is 10.
    long_length : int, optional
        The period for the long EMA. Default is 21.
    source_col : str, optional
        The name of the column to calculate the PO on. Default is 'close'.

    Returns:
    -------
    pd.DataFrame
        The original DataFrame with an added 'PO' column.

    Example Usage:
    --------------
    ```python
    data = calculate_percentage_oscillator(data, short_length=10, long_length=21)
    ```
    """
    short_ema = data[source_col].ewm(span=short_length, adjust=False).mean()
    long_ema = data[source_col].ewm(span=long_length, adjust=False).mean()
    data['PO'] = (short_ema - long_ema) / long_ema * 100
    return data
