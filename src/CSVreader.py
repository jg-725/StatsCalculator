import csv
from FileUtilities.absolutePath import absolutepath


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(absolutepath(filepath)) as dataText:
            csv_data = csv.DictReader(dataText, delimiter=',')

            for row in csv_data:
                self.data.append(row)

        pass