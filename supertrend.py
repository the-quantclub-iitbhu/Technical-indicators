import numpy as np
import pandas as pd

def calculate_supertrend(data, atr_period, factor):
    """
    Calculate the Supertrend indicator for financial time series data.

    The Supertrend is a trend-following indicator that uses the Average True Range (ATR) 
    and price action to identify the direction of the trend and potential reversals.

    Parameters:
    -----------
    data : pandas.DataFrame
        A DataFrame containing the time series data with columns: 'high', 'low', and 'close'.
    atr_period : int
        The period for calculating the Average True Range (ATR).
    factor : float
        The multiplier for the ATR used to calculate the upper and lower bands.

    Returns:
    --------
    pandas.DataFrame
        The input DataFrame with additional columns:
        - 'prev_close': Previous close price.
        - 'tr': True range for each period.
        - 'ATR': Average True Range over the specified period.
        - 'hl2': Midpoint of the high and low prices.
        - 'upper_band': Upper band of the Supertrend.
        - 'lower_band': Lower band of the Supertrend.
        - 'supertrend_l': Supertrend values for the trend direction.
        - 'supertrend_s': Smoothed Supertrend values.

    Example:
    --------
    >>> data = pd.DataFrame({
    >>>     'high': [110, 112, 115],
    >>>     'low': [105, 107, 110],
    >>>     'close': [108, 111, 114]
    >>> })
    >>> atr_period = 7
    >>> factor = 3
    >>> result = calculate_supertrend(data, atr_period, factor)
    >>> print(result)

    References:
    -----------
    - Supertrend Indicator: https://www.investopedia.com/terms/s/supertrend.asp

    """
    df = data.copy()
    high = df['high']
    low = df['low']
    close = df['close']

    # Calculate previous close, true range, and Average True Range (ATR)
    df['prev_close'] = close.shift(1)
    df['tr'] = np.maximum((high - low), 
                          np.maximum(np.abs(high - df['prev_close']), 
                                     np.abs(low - df['prev_close'])))
    df['ATR'] = df['tr'].rolling(window=atr_period).mean()

    # Calculate upper and lower bands
    df['hl2'] = (df['high'] + df['low']) / 2
    df['upper_band'] = df['hl2'] + factor * df['ATR']
    df['lower_band'] = df['hl2'] - factor * df['ATR']

    # Initialize Supertrend columns
    df['supertrend_l'] = 0.0

    # Column index for faster computation
    idx_supertrend = df.columns.get_loc('supertrend_l')
    idx_upband = df.columns.get_loc('upper_band')
    idx_lowband = df.columns.get_loc('lower_band')
    idx_close = df.columns.get_loc('close')

    # Set initial Supertrend value
    df.iloc[0, idx_supertrend] = df['upper_band'].iloc[0]

    # Calculate Supertrend values
    for index in range(1, len(df)):
        if df.iloc[index, idx_close] > df.iloc[index - 1, idx_supertrend]:
            df.iloc[index, idx_supertrend] = df.iloc[index, idx_upband]
        else:
            df.iloc[index, idx_supertrend] = df.iloc[index, idx_lowband]

    # Add smoothed Supertrend column
    df['supertrend_s'] = df['supertrend_l']

    return df
  
