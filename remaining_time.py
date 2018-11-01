from datetime import datetime
import time

def remaining_time(age=0, life_expectancy=80):
    now_dt = datetime.now()
    death_dt = datetime(life_expectancy - age + now_dt.year, now_dt.month, now_dt.day)
    return f'{int((death_dt - now_dt).total_seconds()):,}'

while 1:
    print(remaining_time(26, 80))
    time.sleep(1)