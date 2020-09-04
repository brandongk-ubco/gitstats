from .mocks import MockStatsCollector
from gitstats import StatsCalculator


class TestStatsCalculator:

    def test_all_empty(self):
        collector = MockStatsCollector()
        calculator = StatsCalculator(collector)

        assert len(calculator.getPRsByAssignee()) == 0
        assert len(calculator.getCommentsByUser()) == 0
        assert len(calculator.getCommentsByUserAndPR()) == 0
        assert len(calculator.getCommitsByUser()) == 0
        assert len(calculator.getCommitsByUserAndPR()) == 0
        assert len(calculator.getContributionsByUserAndPR()) == 0
