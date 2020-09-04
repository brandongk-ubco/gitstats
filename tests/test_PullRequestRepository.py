from gitstats.PullRequestRepository import PullRequestRepository
from datetime import datetime, timezone, timedelta
from random import randint
import pytest


class MockRepository:

    def __init__(self, prs=[]):
        self.prs = prs

    def get_pulls(self, *args, **kwargs):
        return self.prs

    def get_pull(self, id: int):
        pr = [p for p in self.prs if p.number == id]
        if len(pr) == 0:
            raise ValueError("PR does not exist")
        if len(pr) > 1:
            raise ValueError("Multiple PRs exist")
        return pr[0]


class MockPR:

    def __init__(self,
                 updated_at=datetime.now(timezone.utc),
                 assignee=None,
                 merged=False,
                 number=randint(1, 1e100),
                 reviews=[],
                 commits=[],
                 issue_comments=[],
                 review_comments=[]):
        self.updated_at = updated_at
        self.assignee = assignee
        self.merged = merged
        self.number = number
        self.reviews = reviews
        self.commits = commits
        self.issue_comments = issue_comments
        self.review_comments = review_comments

    def get_reviews(self):
        return self.reviews

    def get_commits(self):
        return self.commits

    def get_review_comments(self):
        return self.review_comments

    def get_issue_comments(self):
        return self.issue_comments


class TestPullRequestRepository:

    def _mock_pr_response(self, expected_prs=[]):
        repository = MockRepository(expected_prs)
        finder = PullRequestRepository(repository)
        return finder

    @pytest.mark.findByDateRange
    def test_no_prs(self):
        expected_prs = []
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=7)
        prs = finder.findByDateRange(start, end)
        assert len(prs) == 0

    @pytest.mark.findByDateRange
    def test_one_pr(self):
        expected_prs = [MockPR()]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=7)
        prs = finder.findByDateRange(start, end)
        assert len(prs) == len(expected_prs)

    @pytest.mark.findByDateRange
    def test_two_prs(self):
        expected_prs = [MockPR(), MockPR()]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=7)
        prs = finder.findByDateRange(start, end)
        assert len(prs) == 2

    @pytest.mark.findByDateRange
    def test_starts_at_right_date(self):
        expected_prs = [
            MockPR(),
            MockPR(updated_at=datetime.now(timezone.utc) - timedelta(days=10))
        ]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=7)
        prs = finder.findByDateRange(start, end)
        assert len(prs) == 1

    @pytest.mark.findByDateRange
    def test_skips_after_end_date(self):
        expected_prs = [
            MockPR(updated_at=datetime.now(timezone.utc) + timedelta(days=1)),
            MockPR()
        ]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=7)
        prs = finder.findByDateRange(start, end)
        assert len(prs) == 1

    @pytest.mark.getById
    def test_returns_get_pull_response(self):
        expected_prs = [MockPR()]
        finder = self._mock_pr_response(expected_prs)
        pr = finder.getById(expected_prs[0].number)
        assert pr == expected_prs[0]