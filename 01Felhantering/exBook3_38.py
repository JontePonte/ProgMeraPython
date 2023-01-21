# Read from file downloaded from github

import csv


def read_data(filename):
    try:
        with open(filename, newline='') as csv_file:
            try:
                reader = csv.reader(csv_file) # create iterable object from file
                header = next(reader)
                table = [[float(item) for item in row] for row in reader]
                return header, table

            except Exception as e:
                print('csv file could not be read')
                print(e)


    except Exception as e:
        print('something went wrong when loading csv file')
        print(e)


def query_data(table, t):
    try:
        return [row for row in table if row[1] > t]
    except Exception as e:
        print('something went wrong when querying data')
        print(e)


def write_data(header, table, filename):
    try:
        with open(filename, 'w', newline='') as new_file:
            writer = csv.writer(new_file)
            try:
                writer.writerow(header)
            except Exception as e:
                print('Header could not be written to file')
                print(e)
            try:
                for row in table:
                    writer.writerow(row)
            except Exception as e:
                print('Table could not be written to file')
                print(e)
    except Exception as e:
        print('could not write data to file')
        print(e)


header, table = read_data('faithful.csv')
new_table = query_data(table, 4.5)
write_data(header, new_table, "faithful_max_4_5.csv")
