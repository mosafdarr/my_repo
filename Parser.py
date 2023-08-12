import csv
import glob
import calendar

from datetime import datetime

MIN_TEMP = {}
MAX_TEMP = {}
MIN_HUMIDITY = {}
MAX_HUMIDITY = {}
MEAN_HUMIDITY = {}

MONTHS = list(calendar.month_abbr)[1:]


class Parser:
    def __init__(self):
        self.dict_data = {}
        self.parse_data()
    
    def read_files(self):
        years = range(2004, 2017)

        for year in years:
            self.dict_data[year] = {}
            for month in MONTHS:
                self.dict_data[year][month] = []
                globs = glob.glob("**/Murree_weather_*.txt")
                for file_path in globs:
                    with open(file_path, "r") as file:
                        csv_reader = csv.DictReader(file)
                        for row in csv_reader:
                            if row.get("PKT"):
                                date = datetime.strptime(str(row["PKT"]), "%Y-%m-%d")
                            else:
                                date = datetime.strptime(str(row["PKST"]), "%Y-%m-%d")
                            self.dict_data.setdefault(date.year, {}).setdefault(date.month, []).append(row)         

        return self.dict_data

    def parse_data(self):
        self.read_files()
        for year, months in self.dict_data.items():
            MIN_TEMP[year] = {}
            MAX_TEMP[year] = {}
            MIN_HUMIDITY[year] = {}
            MAX_HUMIDITY[year] = {}
            MEAN_HUMIDITY[year] = {}

            for month in months:
                if self.dict_data[year][month]:
                    MIN_TEMP[year][month] = {}
                    MAX_TEMP[year][month] = {}
                    MIN_HUMIDITY[year][month] = {}
                    MAX_HUMIDITY[year][month] = {}
                    MEAN_HUMIDITY[year][month] = {}

                for days in self.dict_data[year][month]:
                    flag_for_pkt = days.get("PKT")
                    flag_for_pkst = days.get("PKST")

                    if flag_for_pkt is not None:
                        day = int(flag_for_pkt.split("-")[2])
                        MIN_TEMP[year][month][day] = days.get("Min TemperatureC")
                        MAX_TEMP[year][month][day] = days.get("Max TemperatureC")
                        MIN_HUMIDITY[year][month][day] = days.get(" Min Humidity")
                        MAX_HUMIDITY[year][month][day] = days.get("Max Humidity")
                        MEAN_HUMIDITY[year][month][day] = days.get(" Mean Humidity")

                    if flag_for_pkst is not None:
                        day = int(flag_for_pkst.split("-")[2])
                        MIN_TEMP[year][month][day] = days.get("Min TemperatureC")
                        MAX_TEMP[year][month][day] = days.get("Max TemperatureC")
                        MIN_HUMIDITY[year][month][day] = days.get(" Min Humidity")
                        MAX_HUMIDITY[year][month][day] = days.get("Max Humidity")
                        MEAN_HUMIDITY[year][month][day] = days.get(" Mean Humidity")

        return True
