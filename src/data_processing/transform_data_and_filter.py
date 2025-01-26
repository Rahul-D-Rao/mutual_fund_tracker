def clean_data(data):
    """
    Clean the mutual fund data.

    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    data = data.dropna()  # Remove rows with missing values
    data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]
    print("Data cleaned successfully.")
    return data
    
def filter_by_date(data, start_date, end_date):
    """
    Filter data within the specified date range.

    Args:
        data (pd.DataFrame): The dataset.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: Filtered data.
    """
    data['date'] = pd.to_datetime(data['date'])
    filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]
    print(f"Data filtered between {start_date} and {end_date}.")
    return filtered_data