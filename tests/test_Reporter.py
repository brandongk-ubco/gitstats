from gitstats import Reporter
from .mocks import MockTemplate, MockStatsCalculator


class TestReporter:

    def test_report(self):
        template = MockTemplate()
        calculator = MockStatsCalculator()
        reporter = Reporter("test", template, calculator)
        assert reporter.report(
        ) == "group_nametest-startstart-endend-contributionscontributions-efforteffort"
