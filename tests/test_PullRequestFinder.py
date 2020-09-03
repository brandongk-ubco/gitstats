from gitstats.PullRequestFinder import PullRequestFinder
from datetime import datetime, timezone, timedelta
import json
import os
import pathlib
from random import randint
from github.PullRequest import PullRequest

current_file = pathlib.Path(__file__).parent.absolute()

class MockRepository:

    def __init__(self, prs=[]):
        self.prs = prs

    def get_pulls(self, *args, **kwargs):
        return self.prs

class MockPR:
    def __init__(self, updated_at=datetime.now(timezone.utc), assignee=None, merged=False, number=randint(1,1e100)):
        self.updated_at = updated_at
        self.assignee = assignee
        self.merged = merged
        self.number = number

class TestPullRequestFinder:

    def _mock_pr_response(self, expected_prs=[]):
        repository = MockRepository(expected_prs)
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=7)
        finder = PullRequestFinder(repository)
        return finder.find(start, end)

    def test_no_prs(self):
        prs = self._mock_pr_response()
        assert len(prs) == 0

    def test_one_pr(self):
        expected_prs = [MockPR()]
        prs = self._mock_pr_response(expected_prs)
        assert len(prs) == len(expected_prs)

    def test_two_prs(self):
        expected_prs = [MockPR(), MockPR()]
        prs = self._mock_pr_response(expected_prs)
        assert len(prs) == 2

    def test_starts_at_right_date(self):
        expected_prs = [MockPR(), MockPR(updated_at=datetime.now(timezone.utc) - timedelta(days=10))]
        prs = self._mock_pr_response(expected_prs)
        assert len(prs) == 1

    def test_skips_after_end_date(self):
        expected_prs = [MockPR(updated_at=datetime.now(timezone.utc) + timedelta(days=1)), MockPR()]
        prs = self._mock_pr_response(expected_prs)
        assert len(prs) == 1