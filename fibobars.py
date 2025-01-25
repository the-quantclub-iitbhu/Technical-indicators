def calculate_fibobars(data, period, fibo_level):
    """
    Calculates the Fibonacci Bars indicator for a given DataFrame.

    The Fibonacci Bars indicator uses Heikin-Ashi candle data to determine trends 
    based on Fibonacci retracement levels.

    Parameters:
    ----------
    data : pd.DataFrame
        A DataFrame containing Heikin-Ashi columns ('ha_high', 'ha_low', 'ha_close', 'ha_open').
    period : int
        The lookback period for calculating the highest high and lowest low.
    fibo_level : float
        The Fibonacci retracement level (e.g., 0.618 for 61.8%).

    Returns:
    -------
    pd.Series
        A series representing the trend values (1 = uptrend, -1 = downtrend).

    Example Usage:
    --------------
    ```python
    data['Fibobars_Trend'] = calculate_fibobars(data, period=14, fibo_level=0.618)
    ```
    """
    highest_high = data['ha_high'].rolling(window=period).max()
    lowest_low = data['ha_low'].rolling(window=period).min()
    trend = []

    for i in range(len(data)):
        if i < period:
            trend.append(0)
        else:
            previous_trend = trend[-1]
            highest_h = highest_high[i]
            lowest_l = lowest_low[i]
            close = data.loc[i, 'ha_close']
            open_price = data.loc[i, 'ha_open']

            # Calculate trend1 and trend2
            trend1 = 1 if (previous_trend >= 0 and
                           ((highest_h - lowest_l) * fibo_level < (close - lowest_l))) else -1
            trend2 = -1 if (previous_trend <= 0 and
                            ((highest_h - lowest_l) * fibo_level < (highest_h - close))) else 1

            # Assign trend based on candle type
            if open_price > close:
                trend.append(trend1)
            else:
                trend.append(trend2)

    return pd.Series(trend, index=data.index)
