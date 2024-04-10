import csv
import pandas as pd
import numpy as np

def read_csv(filepath):
    """
    https://medium.com/casual-inference/the-most-time-efficient-ways-to-import-csv-data-in-python-cc159b44063d
    csv.reader() -
        -
    csv.DictReader() -
    pandas.read_csv() -
        https://gouthamanbalaraman.com/blog/distributed-processing-pandas.html
    dask.dataframe.read_csv() -
        https://pythondata.com/dask-large-csv-python/
    paratext.load_csv_to_direct() -
    paratext.load_csv_to_pandas() -
    datatable -
    :param filepath:
    :return:
    """
    with open(file= filepath, mode= 'r', encoding='UTF-8') as csvfile:
        csv_rows = csv.reader(csvfile, delimiter=',')
        for rows in csv_rows:
            print(rows)

def write_csv(filepath, fields, country_list, country_dict):
    # Write mode - List of List
    with open(file=filepath, mode='w', encoding='UTF-8', newline= '') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(fields)
        csv_writer.writerows(country_list)

    # Append Mode - List of Dict
    with open(file=filepath, mode='a', encoding='UTF-8', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fields)
        csv_writer.writerows(country_dict)

if __name__ == "__main__":
    read_csv(r'Analytics\sample.csv.txt')
    fields_list = ['id', 'country', 'description']
    country_list = [['1', 'USA','The United States is a highly developed country that has the highest median income of any polity in the world.'],
    ['2', 'India','India is a country in South Asia.It is the seventh-largest country by area and most populous country.'],
    ['3', 'Canada','Canada is a country in North America. Its ten provinces and three territories extend from the Atlantic Ocean to the Pacific Ocean.']]
    country_dict = [{'id': '4', 'country': 'Mexico', 'description':'Mexico is a country in the southern portion of North America.'}]
    write_csv(r'Analytics\country.csv.txt', fields_list, country_list, country_dict)