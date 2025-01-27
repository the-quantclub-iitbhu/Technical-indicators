import numpy as np
import pandas as pd

def kalman_filter(data, column, process_variance=1e-1, measurement_variance=1):
    """
    Applies a Kalman Filter to smooth the given column of a DataFrame.

    The Kalman Filter uses prediction and measurement updates to iteratively 
    refine estimates of a system's state (e.g., smoothed price) in the presence 
    of uncertainty or noise.

    Parameters:
    ----------
    data : pd.DataFrame
        The input DataFrame containing the column to smooth.
    column : str
        The name of the column to apply the Kalman Filter on (e.g., 'close', 'open').
    process_variance : float, optional
        The variance in the process (default is 1e-1).
    measurement_variance : float, optional
        The variance in the measurements (default is 1).

    Returns:
    -------
    pd.Series
        A Series containing the smoothed values for the specified column.

    Example Usage:
    --------------
    ```python
    data['smoothed_close'] = kalman_filter(data, 'close')
    data['smoothed_open'] = kalman_filter(data, 'open')
    ```
    """
    # Initialize Kalman Filter variables
    posteri_estimate = 0.0  # Initial estimate of the system's state
    posteri_error_estimate = 1.0  # Initial estimate of the state uncertainty
    smoothed_values = []  # List to store the smoothed values

    # Loop through each value in the specified column
    for value in data[column]:
        # Prediction update (time update)
        priori_estimate = posteri_estimate  # Prior estimate
        priori_error_estimate = posteri_error_estimate + process_variance  # Prior error estimate

        # Measurement update (correction step)
        kalman_gain = priori_error_estimate / (priori_error_estimate + measurement_variance)  # Kalman gain
        posteri_estimate = priori_estimate + kalman_gain * (value - priori_estimate)  # Update estimate
        posteri_error_estimate = (1 - kalman_gain) * priori_error_estimate  # Update error estimate

        # Append the smoothed value to the list
        smoothed_values.append(posteri_estimate)

    return pd.Series(smoothed_values, index=data.index)

# Example usage
# Create a sample DataFrame
data = pd.DataFrame({
    'close': [100, 101, 102, 105, 104, 106, 108, 107],
    'open': [99, 100, 101, 103, 102, 104, 106, 105]
})

# Apply Kalman Filter on 'close' and 'open' columns
data['smoothed_close'] = kalman_filter(data, 'close')
data['smoothed_open'] = kalman_filter(data, 'open')

# Display the DataFrame
print(data)
