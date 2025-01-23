import numpy as np
import pandas as pd

def calculate_dirmov(high, low, length):
    """
    Calculate the Directional Movement (DM) and Directional Indicator (DI).

    This function computes the +DI (Positive Directional Indicator) and 
    -DI (Negative Directional Indicator) based on the True Range and 
    directional movements of the high and low prices.

    Parameters:
    ----------
    high : pandas.Series
        A series of high prices.
    low : pandas.Series
        A series of low prices.
    length : int
        The look-back period for calculating moving averages.

    Returns:
    -------
    plusDI : pandas.Series
        The Positive Directional Indicator (+DI).
    minusDI : pandas.Series
        The Negative Directional Indicator (-DI).

    Notes:
    ------
    - The function uses the True Range (TR) as the denominator for 
      calculating the Directional Indicators.
    - If `length` is too small, the results may not be smooth.

    Example:
    --------
    >>> high = pd.Series([120, 121, 122, 123, 124])
    >>> low = pd.Series([119, 118, 117, 116, 115])
    >>> calculate_dirmov(high, low, 14)
    (plusDI, minusDI)

    """
    # Calculate upward and downward movements
    up = high.diff()
    down = -low.diff()

    # Calculate the Positive and Negative Directional Movements
    plusDM = np.where((up > down) & (up > 0), up, 0)
    minusDM = np.where((down > up) & (down > 0), down, 0)

    # Compute the True Range (TR) using a helper function (ensure it's implemented)
    tr = calculate_true_range(high, low, high).rolling(length).mean()

    # Calculate the Positive and Negative Directional Indicators
    plusDI = 100 * pd.Series(plusDM).rolling(length).mean() / tr
    minusDI = 100 * pd.Series(minusDM).rolling(length).mean() / tr

    # Fill missing values with 0
    plusDI = plusDI.fillna(0)
    minusDI = minusDI.fillna(0)

    return plusDI, minusDI
