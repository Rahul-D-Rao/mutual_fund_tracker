import pandas as pd

def load_mutual_fund_data(file_path):
    """
    Load mutual fund data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}")
        return data
    except Exception as e:
        raise ValueError(f"Failed to load data from {file_path}: {e}")