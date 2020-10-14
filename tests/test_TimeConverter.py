from gitstats import TimeConverter
from datetime import datetime, timedelta


class TestTimeConverter:

    def testPST(self):
        date = datetime.fromisoformat("2020-12-12T10:30")
        assert TimeConverter.utc_to_pacific(date) == datetime.fromisoformat(
            "2020-12-12T18:30")

    def testPDT(self):
        date = datetime.fromisoformat("2020-10-12T10:30")
        assert TimeConverter.utc_to_pacific(date) == datetime.fromisoformat(
            "2020-10-12T17:30")