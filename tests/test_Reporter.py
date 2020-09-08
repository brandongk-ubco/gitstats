from gitstats import Reporter
from .mocks import MockTemplate, MockStatsCalculator


class TestReporter:

    def test_report(self):
        template = MockTemplate()
        calculator = MockStatsCalculator()
        reporter = Reporter("test", template, calculator)
        assert reporter.report() == "{}{}".format(
            "group_nametest-startstart-endend-contributionscontributions",
            "-efforteffort-issues['issues']-excluded_issues['excluded_issues']-team_scoreteamscore-final_scoresfinalscores"
        )
