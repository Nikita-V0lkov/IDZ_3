import pandas as pd


def search_for_nan(csv_dataframe):
    """
    Function return sum of nan in the dataframe

    Parameters
    ----------
    :param csv_dataframe : dataframe
        Dataframe which we get from *.csv

    Returns
    -------
    :return sum_all_nans : series
        Sum of nan in the dataframe
    """
    if not isinstance(csv_dataframe, pd.DataFrame):
        raise TypeError('Only dataframe type accepted')

    sum_all_nans = csv_dataframe.isna().sum()
    return sum_all_nans


def search_for_max_nan(csv_dataframe):
    """
    Function return column with the maximum number of nan

    Parameters
    ----------
    :param csv_dataframe : dataframe
        Dataframe which we get from *.csv

    Returns
    -------
    :return max_nan_column : str
        Column with the maximum number of nan
    """
    if not isinstance(csv_dataframe, pd.DataFrame):
        raise TypeError('Only dataframe type accepted')

    max_nan_column = csv_dataframe.isna().sum().idxmax()
    return max_nan_column


def drop_all_nans(csv_dataframe):
    """
    Function remove all rows with nan

    Parameters
    ----------
    :param csv_dataframe : dataframe
        Dataframe which we get from *.csv

    Returns
    -------
    :return csv_dataframe_wo_nan : dataframe
        Dataframe without nan rows
    """
    if not isinstance(csv_dataframe, pd.DataFrame):
        raise TypeError('Only dataframe type accepted')

    csv_dataframe_wo_nan = csv_dataframe.dropna()
    return csv_dataframe_wo_nan


def delete_frequent_null(csv_dataframe):
    """
    Function remove column with most frequent nan

    Parameters
    ----------
    :param csv_dataframe : dataframe
        Dataframe which we get from *.csv

    Returns
    -------
    :return csv_dataframe : dataframe
        Dataframe without most frequent nan column
    """
    if not isinstance(csv_dataframe, pd.DataFrame):
        raise TypeError('Only dataframe type accepted')

    del csv_dataframe[search_for_max_nan(csv_dataframe)]
    return csv_dataframe


def group_by_sex_and_age(csv_dataframe):
    """
    Function which group data for women, men and children

    Parameters
    ----------
    :param csv_dataframe : dataframe
        Dataframe which we get from *.csv

    Returns
    -------
    :return grouped_data : dataframe
        Dataframe with grouped data for women, men and children
    """
    if not isinstance(csv_dataframe, pd.DataFrame):
        raise TypeError('Only dataframe type accepted')

    people_data = pd.DataFrame(csv_dataframe)
    children_data = pd.DataFrame(csv_dataframe['Age'] < 18)
    people_data['Child'] = children_data
    grouped_data = people_data.sort_values(by=['Sex'])
    return grouped_data
