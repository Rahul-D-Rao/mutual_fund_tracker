def export_to_csv(data, output_path):
    """
    Export the processed data to a CSV file.

    Args:
        data (pd.DataFrame): Processed data.
        output_path (str): File path to save the CSV.

    Returns:
        None
    """
    data.to_csv(output_path, index=False)
    print(f"Data successfully exported to {output_path}.")