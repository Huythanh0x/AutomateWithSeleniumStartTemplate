from datetime import datetime
from datetime import timedelta

date_time_format = '%Y-%m-%d %H:%M:%S'
hour_time_format = '%I:%M %p'
fifteen_minutes = timedelta(minutes=15)
zero_minute = timedelta(minutes=0)

class DateTimeHelper():
    def __init__(self, date_time_format, hour_time_format) -> None:
        self.date_time_format = date_time_format
        self.hour_time_format = hour_time_format

    def get_time_remain_to(self,destinated_date_time_str):
        return self.conver_str_date_time_to_date_time_format(destinated_date_time_str) - self.get_current_date_time_in_scheduled_format()


    def get_current_date_time_in_scheduled_format(self):
        current_datetime_str = datetime.today().strftime(self.date_time_format)
        current_date_time = self.conver_str_date_time_to_date_time_format(
            current_datetime_str)
        return current_date_time


    def conver_str_date_time_to_hour_time_format(self, date_time_str):
        return self.conver_str_time_to_another_format(date_time_str, self.hour_time_format)


    def conver_str_date_time_to_date_time_format(self, date_time_str):
        return self.conver_str_time_to_another_format(date_time_str, self.date_time_format)


    def conver_str_time_to_another_format(self, date_time_str, another_date_time_format):
        return datetime.strptime(date_time_str, another_date_time_format)
