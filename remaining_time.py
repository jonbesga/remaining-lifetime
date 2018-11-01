from datetime import datetime
import time
import csv

FILE_PATH = 'life_expectancy_country.csv'
COUNTRY_COLUMN = 'Country and regions'
FEMALE_SEX_COLUMN = 'Female life expectancy'
MALE_SEX_COLUMN = 'Male life expectancy'

LIFE_EXPECTANCY_DB = {}

def populate_life_expectancy_db():
    with open(FILE_PATH, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            LIFE_EXPECTANCY_DB[row[COUNTRY_COLUMN].lower()] = {
                'm': int(float(row[MALE_SEX_COLUMN])),
                'f': int(float(row[FEMALE_SEX_COLUMN]))
            }

def get_life_expectancy(country, sex):
    return LIFE_EXPECTANCY_DB[country][sex]


def remaining_time(age, country, sex):
    now_dt = datetime.now()
    life_expectancy = get_life_expectancy(country, sex)
    death_dt = datetime(life_expectancy - age + now_dt.year, now_dt.month, now_dt.day)
    return f'{int((death_dt - now_dt).total_seconds()):,}'

populate_life_expectancy_db()

while 1:
    print(remaining_time(26, 'united kingdom', 'm'))
    time.sleep(1)