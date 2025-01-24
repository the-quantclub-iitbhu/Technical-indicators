def calculate_obv(data):
    """
    Calculate the On-Balance Volume (OBV).

    OBV is a momentum indicator that uses volume flow to predict changes in stock price.

    Parameters:
    ----------
    data : pandas.DataFrame
        A DataFrame containing at least the 'close' and 'volume' columns.

    Returns:
    -------
    obv : pandas.Series
        The On-Balance Volume values.
    """
    obv = np.zeros(len(data))
    for i in range(1, len(data)):
        if data['close'].iloc[i] > data['close'].iloc[i - 1]:
            obv[i] = obv[i - 1] + data['volume'].iloc[i]
        elif data['close'].iloc[i] < data['close'].iloc[i - 1]:
            obv[i] = obv[i - 1] - data['volume'].iloc[i]
        else:
            obv[i] = obv[i - 1]
    return pd.Series(obv, index=data.index)
