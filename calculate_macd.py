def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    """
    Calculate the Moving Average Convergence Divergence (MACD) indicator.

    Parameters:
    ----------
    data : pandas.DataFrame
        A DataFrame containing at least the 'close' column with closing prices of the asset.
    short_window : int, optional
        The period for the short-term exponential moving average (EMA). Default is 12.
    long_window : int, optional
        The period for the long-term exponential moving average (EMA). Default is 26.
    signal_window : int, optional
        The period for the signal line EMA. Default is 9.

    Returns:
    -------
    macd_line : pandas.Series
        The MACD line (difference between short-term and long-term EMAs).
    signal_line : pandas.Series
        The signal line (EMA of the MACD line).
    """
    exp1 = data['close'].ewm(span=short_window, adjust=False).mean()
    exp2 = data['close'].ewm(span=long_window, adjust=False).mean()
    macd_line = exp1 - exp2
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()
    return macd_line, signal_line
