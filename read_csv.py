#This module convert a file csv in a dictionary of python

import csv #It's very useful import this module for work with csv
import json

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key:value for key,value in iterable}
            data.append(country_dict)

        return data

def convert_json(dict, path):
    with open(path, 'w') as file:
        json.dump(dict, file)


def main():
    data = read_csv('main/app/data.csv')
    convert_json(data, 'main/app/data.json')

if __name__ == '__main__':
    main()
    