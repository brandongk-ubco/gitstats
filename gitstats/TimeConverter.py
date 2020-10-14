import pytz
from datetime import timedelta


class TimeConverter:

    @staticmethod
    def utc_to_pacific(dt):
        vancouver = pytz.timezone('America/Vancouver')
        offset = round(vancouver.utcoffset(dt).total_seconds() / 3600, 0)
        return dt - timedelta(hours=offset)
