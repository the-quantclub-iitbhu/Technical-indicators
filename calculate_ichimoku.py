def calculate_ichimoku(data, conversion_periods, base_periods, lagging_span2_periods):
    """
    Calculates the Ichimoku Kinko Hyo components.

    The Ichimoku indicator consists of:
    - Conversion Line (Tenkan-sen): Midpoint of the highest high and lowest low over the conversion period.
    - Base Line (Kijun-sen): Midpoint of the highest high and lowest low over the base period.
    - Leading Span 1 (Senkou Span A): Average of Conversion and Base Lines, plotted in the future.
    - Leading Span 2 (Senkou Span B): Midpoint of the highest high and lowest low over the lagging span 2 period.

    Parameters:
    ----------
    data : pd.DataFrame
        A DataFrame containing 'high' and 'low' columns.
    conversion_periods : int
        Lookback period for the Conversion Line.
    base_periods : int
        Lookback period for the Base Line.
    lagging_span2_periods : int
        Lookback period for the Leading Span 2.

    Returns:
    -------
    tuple
        A tuple containing the following components:
        - Conversion Line (pd.Series)
        - Base Line (pd.Series)
        - Lead Line 1 (pd.Series)
        - Lead Line 2 (pd.Series)

    Example Usage:
    --------------
    ```python
    conversion, base, lead1, lead2 = calculate_ichimoku(data, 9, 26, 52)
    data['Conversion_Line'] = conversion
    data['Base_Line'] = base
    data['Lead_Line1'] = lead1
    data['Lead_Line2'] = lead2
    ```
    """
    # Conversion Line (Tenkan-sen)
    conversion_line = donchian(data, conversion_periods)

    # Base Line (Kijun-sen)
    base_line = donchian(data, base_periods)

    # Leading Span 1 (Senkou Span A)
    lead_line1 = (conversion_line + base_line) / 2

    # Leading Span 2 (Senkou Span B)
    lead_line2 = (
        data['low'].rolling(window=lagging_span2_periods).min() +
        data['high'].rolling(window=lagging_span2_periods).max()
    ) / 2

    return conversion_line, base_line, lead_line1, lead_line2
