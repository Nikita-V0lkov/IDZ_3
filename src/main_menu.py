from get_from_csv import *
from check_and_group_csv import *


def main_menu():
    titanic_dt_csv = get_from_csv()
    print("Source csv:\n", titanic_dt_csv)
    print("Number of nans in dataframe:\n", search_for_nan(titanic_dt_csv))
    print("Column with max nan:", search_for_max_nan(titanic_dt_csv))
    print("Dropped all nans:\n", drop_all_nans(titanic_dt_csv))
    print("Dataframe in which deleted column with frequent nan:\n", delete_frequent_null(titanic_dt_csv))
    print("Grouped by sex and age:\n", group_by_sex_and_age(titanic_dt_csv))
