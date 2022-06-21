import pandas as pd


def get_from_csv():
    """
    Function gets values from *.csv and passes them to dataframe

    Returns
    -------
    :return : titanic_dt: dataframe
        Dataframe received from *.csv
    """
    try:
        titanic_dt = pd.read_csv('titanic.csv', sep=';')
        return titanic_dt
    except FileNotFoundError:
        print('File doesnt exist or you dont have permission to read it')
