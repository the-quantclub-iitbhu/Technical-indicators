def calculate_bollinger_bands(data, window=20, num_sd=2):
    """
    Calculate Bollinger Bands for a given financial time series dataset.

    Bollinger Bands are volatility bands placed above and below a simple moving average (SMA).
    They provide an indication of relative price levels over a specified period.

    Parameters:
    ----------
    data : pandas.DataFrame
        A DataFrame containing at least the 'close' column with closing prices of the asset.
    window : int, optional
        The rolling window period used to calculate the simple moving average (SMA) and rolling standard deviation. 
        Default is 20.
    num_sd : float, optional
        The number of standard deviations to determine the upper and lower bands. Default is 2.

    Returns:
    -------
    upper_band : pandas.Series
        The upper Bollinger Band values.
    lower_band : pandas.Series
        The lower Bollinger Band values.

    Example:
    -------
    >>> import pandas as pd
    >>> data = pd.DataFrame({'close': [100, 102, 104, 103, 101, 105, 110]})
    >>> upper_band, lower_band = calculate_bollinger_bands(data, window=3, num_sd=2)
    >>> print(upper_band)
    >>> print(lower_band)
    """
    sma = data['close'].rolling(window).mean()
    rolling_std = data['close'].rolling(window).std()
    upper_band = sma + (rolling_std * num_sd)
    lower_band = sma - (rolling_std * num_sd)
    return upper_band, lower_band
