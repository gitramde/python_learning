import csv
import pandas as pd
import dask.dataframe
import datatable as dt

def read_csv(filepath):
    """
    https://medium.com/casual-inference/the-most-time-efficient-ways-to-import-csv-data-in-python-cc159b44063d
    csv.reader() - Returns a reader object that can be iterated over to read the entire CSV

    csv.DictReader() - Converts the csv file to dictionary. Takes the first row as the key for dictionary and convert
                       rest of the rows to values.
                       All the fields are imported as a String.

    pandas.read_csv() -
        https://gouthamanbalaraman.com/blog/distributed-processing-pandas.html
        Suited for tabular data with heterogeneously-typed columns
        Can also be used as vectors and matrices
        Preferred for Data Analysis as they are very easy to manipulate and transform

    dask.dataframe.read_csv() - Returns dask dataframe
        https://pythondata.com/dask-large-csv-python/
        unlike pandas with dask the data is not fully loaded into memory, but is ready to be processed.
        most functions used with pandas can be also use with dask.

    datatable


    paratext.load_csv_to_direct() - Not explored here as it is difficult to set up in windows
    paratext.load_csv_to_pandas() - Not explored here as it is difficult to set up in windows

    :param filepath:
    :return:
    """
    # Approach 1
    with open(file= filepath, mode= 'r', encoding='UTF-8') as csvfile:
        csv_rows = csv.reader(csvfile, delimiter=',')
        for rows in csv_rows:
            print(rows)

    # Approach 2a
    with open(file=filepath, mode='r', encoding='UTF-8') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            print(row)

    # Approach 2b
    data = csv.DictReader(open(filepath))
    for row in data:
        print(row)

    # Approach 3 (Pandas)
    data = pd.read_csv(filepath)
    print(data)

    # Approach 4 (Pandas with Chunksize)
    chunks = pd.read_csv(filepath, chunksize=100000)
    data = pd.concat(chunks)
    print(type(data))

    # Approach 5 (Dask Dataframe)
    data = dask.dataframe.read_csv(filepath)
    print(type(data))

    # Approach 6 (Datatable)
    data = dt.fread(filepath)
    print(data)

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