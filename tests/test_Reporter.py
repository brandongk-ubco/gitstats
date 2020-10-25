from gitstats import Reporter
from .mocks import MockTemplate, MockStatsCalculator, MockNormalizer


class TestReporter:

    def test_report(self):
        template = MockTemplate()
        calculator = MockStatsCalculator()
        normalizer = MockNormalizer()
        reporter = Reporter("test", template, calculator, normalizer)
        assert reporter.report() == "{}{}".format(
            "group_nametest-startstart-endend-contributionsByUserAndPRcontributionsByUserAndPR-contributionsByUsercontributionsByUser",
            "-efforteffort-issues['issues']-excluded_issues['excluded_issues']-team_scoreteamscore-final_scoresfinalscores"
        )
