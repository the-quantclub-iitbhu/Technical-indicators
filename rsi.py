import numpy as np
import pandas as pd

def calculate_rsi(df, length):
    """
    Calculate the Relative Strength Index (RSI) for a given dataset.

    Parameters:
    ----------
    df : pandas.DataFrame
        DataFrame containing the 'close' prices column.
    length : int
        The lookback period for calculating RSI.

    Returns:
    -------
    pandas.Series
        A Series containing the RSI values for the specified input data.
    """
    delta = df['close'].diff(1)
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = pd.Series(gain).rolling(window=length).mean()
    avg_loss = pd.Series(loss).rolling(window=length).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
