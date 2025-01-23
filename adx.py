import pandas as pd
import numpy as np

def calculate_adx(data, period=14, smoothing_period=14):
    """
    Calculate the Average Directional Index (ADX) for a given dataset.

    Parameters:
    ----------
    data : pandas.DataFrame
        DataFrame containing 'high', 'low', and 'close' price columns.
    period : int, optional
        The lookback period for calculating TR, DM+, and DM-. Default is 14.
    smoothing_period : int, optional
        The smoothing period for the ADX calculation. Default is 14.

    Returns:
    -------
    pandas.DataFrame
        DataFrame with columns: TR, DM+, DM-, DI+, DI-, DX, and ADX.
    """
    df = data.copy()
    df['TR'] = np.maximum(df['high'] - df['low'], 
                          np.maximum(abs(df['high'] - df['close'].shift()), abs(df['low'] - df['close'].shift())))
    df['DM+'] = np.where((df['high'] - df['high'].shift()) > (df['low'].shift() - df['low']), 
                         np.maximum(df['high'] - df['high'].shift(), 0), 0)
    df['DM-'] = np.where((df['low'].shift() - df['low']) > (df['high'] - df['high'].shift()), 
                         np.maximum(df['low'].shift() - df['low'], 0), 0)
    
    df['TR'] = df['TR'].rolling(window=period).mean()
    df['DM+'] = df['DM+'].rolling(window=period).mean()
    df['DM-'] = df['DM-'].rolling(window=period).mean()

    df['DI+'] = 100 * (df['DM+'] / df['TR'])
    df['DI-'] = 100 * (df['DM-'] / df['TR'])
    df['DX'] = 100 * abs(df['DI+'] - df['DI-']) / (df['DI+'] + df['DI-'])
    df['ADX'] = df['DX'].rolling(window=smoothing_period).mean()
    return df
