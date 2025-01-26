def group_data_by_fund_and_month(data):
    """
    Group data by mutual fund and month.

    Args:
        data (pd.DataFrame): Filtered data.

    Returns:
        pd.DataFrame: Grouped data with totals by fund and month.
    """
    data['month'] = data['date'].dt.to_period('M')
    grouped_data = data.groupby(['fund_name', 'month']).agg({'allocation': 'sum'}).reset_index()
    print("Data grouped by fund and month successfully.")
    return grouped_data