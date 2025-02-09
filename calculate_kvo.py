import pandas as pd

def calculate_kvo(data, short_period=34, long_period=55):
    """
    Calculate the Klinger Volume Oscillator (KVO).
    
    Parameters:
        data (pd.DataFrame): A DataFrame containing 'high', 'low', 'close', and 'volume' columns.
        short_period (int): The period for the short-term EMA (default: 34).
        long_period (int): The period for the long-term EMA (default: 55).
    
    Returns:
        pd.DataFrame: Original DataFrame with an added 'KVO' column.
    """
    # Ensure required columns are present
    if not {'high', 'low', 'close', 'volume'}.issubset(data.columns):
        raise ValueError("Data must contain 'high', 'low', 'close', and 'volume' columns.")

    # Calculate Money Flow Multiplier (MFM)
    data['MFM'] = ((data['close'] - data['low']) - (data['high'] - data['close'])) / (data['high'] - data['low'])
    
    # Calculate Money Flow Volume (MFV)
    data['MFV'] = data['MFM'] * data['volume']
    
    # Compute the KVO using EMA
    data['KVO'] = data['MFV'].ewm(span=short_period, adjust=False).mean() - data['MFV'].ewm(span=long_period, adjust=False).mean()

    return data
