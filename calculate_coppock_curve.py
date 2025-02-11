import pandas as pd

def calculate_coppock_curve(data, short_roc=11, long_roc=14, wma_period=10):
    """
    Calculate the Coppock Curve indicator.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing a 'close' column.
        short_roc (int): Period for the short-term Rate of Change (default: 11).
        long_roc (int): Period for the long-term Rate of Change (default: 14).
        wma_period (int): Period for the Weighted Moving Average (default: 10).
    
    Returns:
        pd.DataFrame: Original DataFrame with an added 'CoppockCurve' column.
    """
    # Ensure required column is present
    if 'close' not in data.columns:
        raise ValueError("Data must contain a 'close' column.")

    # Calculate Rate of Change (ROC)
    data['ROC_Short'] = ((data['close'] - data['close'].shift(short_roc)) / data['close'].shift(short_roc)) * 100
    data['ROC_Long'] = ((data['close'] - data['close'].shift(long_roc)) / data['close'].shift(long_roc)) * 100

    # Sum of the two ROC values
    data['ROC_Sum'] = data['ROC_Short'] + data['ROC_Long']

    # Calculate Weighted Moving Average (WMA)
    data['CoppockCurve'] = data['ROC_Sum'].ewm(span=wma_period, adjust=False).mean()

    return data
