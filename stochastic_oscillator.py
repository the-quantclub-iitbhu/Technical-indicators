import pandas as pd

def calculate_stochastic(df, length, smoothing):
    """
    Calculate the Stochastic Oscillator (%K) for a given dataset.

    Parameters:
    ----------
    df : pandas.DataFrame
        DataFrame containing 'low', 'high', and 'close' price columns.
    length : int
        The lookback period for calculating the lowest low and highest high.
    smoothing : int
        The smoothing factor applied to the %K line.

    Returns:
    -------
    pandas.Series
        A Series containing the smoothed %K values of the Stochastic Oscillator.
    """
    lowest_low = df['low'].rolling(window=length).min()
    highest_high = df['high'].rolling(window=length).max()
    stoch_k = 100 * (df['close'] - lowest_low) / (highest_high - lowest_low)
    stoch_k = stoch_k.rolling(window=smoothing).mean()  # Smoothing
    return stoch_k
