import pandas_ta as ta

def calculate_aroon(df, period=14):
    """
    Calculates the Aroon Up and Aroon Down indicators for a given DataFrame using the pandas_ta library.

    The Aroon indicator is a technical analysis tool that measures the time it takes for the 
    highest high or lowest low to occur within a specified period. It is used to identify 
    trends and assess their strength.

    This implementation leverages the `pandas_ta` library for efficient computation.

    Parameters:
    ----------
    df : pd.DataFrame
        A DataFrame containing at least the following columns:
        - 'high': High prices over time.
        - 'low': Low prices over time.
    period : int, optional
        The lookback period for calculating the Aroon indicators. Default is 14.

    Returns:
    -------
    pd.DataFrame
        The original DataFrame with two additional columns:
        - 'Aroon_Up': Strength of the upward trend (0 to 100).
        - 'Aroon_Down': Strength of the downward trend (0 to 100).

    Requirements:
    -------------
    Install the `pandas_ta` library if not already installed:
    ```
    pip install pandas-ta
    ```

    Example Usage:
    --------------
    ```python
    import pandas as pd
    from your_script import calculate_aroon

    # Example DataFrame
    data = pd.DataFrame({
        'high': [1, 2, 3, 4, 5, 4, 3],
        'low': [1, 1, 2, 2, 3, 2, 1]
    })

    # Calculate Aroon indicators
    result = calculate_aroon(data, period=14)
    print(result)
    ```
    """
    # Calculate Aroon Up and Down using pandas_ta
    aroon = ta.aroon(df['high'], df['low'], length=period)

    # Debug: Print the Aroon values (optional)
    print(aroon)

    # Add Aroon Up and Down values to the DataFrame
    df['Aroon_Up'] = aroon['AROONU_14']
    df['Aroon_Down'] = aroon['AROOND_14']

    return df
