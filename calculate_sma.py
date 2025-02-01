import pandas as pd

def calculate_sma(data, column='close', period=14):
    """
    Calculate the Simple Moving Average (SMA).

    Parameters:
    data (pd.DataFrame): DataFrame containing price data.
    column (str): The column name to calculate SMA on (default is 'close').
    period (int): The time period for SMA calculation.

    Returns:
    pd.Series: The SMA values.
    """
    data[f'SMA_{period}'] = data[column].rolling(window=period).mean()
    return data
