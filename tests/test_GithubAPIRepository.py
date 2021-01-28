from gitstats.GithubAPIRepository import GithubAPIRepository
from datetime import datetime, timedelta
import pytest
from .mocks import MockRepository, MockPR, MockReview, MockCommit, MockComment, MockIssue, MockLabel
import logging


class TestGithubAPIRepository:

    def setup_class(self):
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler("TestGithubAPIRepository.log")
        self.logger.setLevel("DEBUG")
        self.logger.addHandler(handler)

    def _mock_pr_response(self, expected_prs=[]):
        repository = MockRepository(expected_prs)
        finder = GithubAPIRepository(repository, logger=self.logger)
        return finder

    def _mock_issue_response(self, expected_issues=[]):
        repository = MockRepository(issues=expected_issues)
        finder = GithubAPIRepository(repository, logger=self.logger)
        return finder

    @pytest.mark.findPRsByDateRange
    def test_no_prs(self):
        expected_prs = []
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 0

    @pytest.mark.findPRsByDateRange
    def test_one_pr(self):
        expected_prs = [MockPR()]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == len(expected_prs)

    @pytest.mark.findPRsByDateRange
    def test_not_merged(self):
        expected_prs = [MockPR()]
        expected_prs[0].closed_at = None
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 0

    @pytest.mark.findPRsByDateRange
    def test_two_prs(self):
        expected_prs = [MockPR(), MockPR()]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 2

    @pytest.mark.findPRsByDateRange
    def test_prs_start_at_right_date(self):
        expected_prs = [
            MockPR(),
            MockPR(updated_at=datetime.now() - timedelta(days=10))
        ]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 1

    @pytest.mark.findPRsByDateRange
    def test_prs_skip_after_end_date(self):
        expected_prs = [
            MockPR(closed_at=datetime.now() + timedelta(days=1)),
            MockPR()
        ]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 1

    @pytest.mark.findPRsByDateRange
    def test_ignores_one_pr(self):
        expected_prs = [MockPR(labels=[MockLabel("gitstats-ignore")])]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 0

    @pytest.mark.findPRsByDateRange
    def test_ignores_one_pr_but_not_both(self):
        expected_prs = [
            MockPR(labels=[MockLabel("gitstats-ignore")]),
            MockPR(labels=[MockLabel("do-not-ignore")])
        ]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 1

    @pytest.mark.getById
    def test_returns_get_pull_response(self):
        expected_prs = [MockPR()]
        finder = self._mock_pr_response(expected_prs)
        pr = finder.getById(expected_prs[0].number)
        assert pr == expected_prs[0]

    @pytest.mark.getReviewsByPullRequestId
    def test_returns_reviews(self):
        expected_reviews = [MockReview(), MockReview()]
        pr = MockPR(reviews=expected_reviews)
        finder = self._mock_pr_response([pr])
        reviews = finder.getReviewsByPullRequestId(pr.number)
        assert len(reviews) == len(expected_reviews)

    @pytest.mark.getCommitsByPullRequestId
    def test_returns_commits(self):
        expected_commits = [MockCommit(), MockCommit()]
        pr = MockPR(commits=expected_commits)
        finder = self._mock_pr_response([pr])
        commits = finder.getCommitsByPullRequestId(pr.number)
        assert len(commits) == len(expected_commits)
        for i in range(0, len(commits)):
            actual_date = commits["date"][i]
            expected_date = expected_commits[i].date
            assert abs(actual_date - expected_date) < timedelta(seconds=1)

    @pytest.mark.getCommitsByPullRequestId
    def test_ignores_merge_commits(self):
        commit_1 = MockCommit()
        commit_2 = MockCommit()
        merge_commit = MockCommit(parents=[commit_1, commit_2])
        expected_commits = [commit_1, commit_2, merge_commit]
        pr = MockPR(commits=expected_commits)
        finder = self._mock_pr_response([pr])
        commits = finder.getCommitsByPullRequestId(pr.number)
        assert len(commits) == 2
        for i in range(0, len(commits)):
            actual_date = commits["date"][i]
            expected_date = expected_commits[i].date
            assert abs(actual_date - expected_date) < timedelta(seconds=1)

    @pytest.mark.getCommentsByPullRequestId
    def test_returns_comments(self):
        expected_review_comments = [MockComment(), MockComment()]
        expected_issue_comments = [MockComment(), MockComment()]
        pr = MockPR(issue_comments=expected_issue_comments,
                    review_comments=expected_review_comments)
        finder = self._mock_pr_response([pr])
        comments = finder.getCommentsByPullRequestId(pr.number)
        assert len(comments) == len(expected_review_comments) + len(
            expected_issue_comments)

    @pytest.mark.findIssuesByDateRange
    def test_no_issues(self):
        expected_issues = []
        finder = self._mock_issue_response(expected_issues)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findIssuesByDateRange(start, end)
        assert len(prs) == 0

    @pytest.mark.findIssuesByDateRange
    def test_one_issue(self):
        expected_issues = [MockIssue()]
        finder = self._mock_issue_response(expected_issues)
        end = datetime.now()
        start = end - timedelta(days=7)
        issues = finder.findIssuesByDateRange(start, end)
        assert len(issues) == len(expected_issues)

    @pytest.mark.findIssuesByDateRange
    def test_two_issues(self):
        expected_issues = [MockIssue(), MockIssue()]
        finder = self._mock_issue_response(expected_issues)
        end = datetime.now()
        start = end - timedelta(days=7)
        issues = finder.findIssuesByDateRange(start, end)
        assert len(issues) == 2

    @pytest.mark.findIssuesByDateRange
    def test_issues_skip_after_end_date(self):
        expected_issues = [
            MockIssue(closed_at=datetime.now() + timedelta(days=1)),
            MockIssue()
        ]
        finder = self._mock_issue_response(expected_issues)
        end = datetime.now()
        start = end - timedelta(days=7)
        issues = finder.findIssuesByDateRange(start, end)
        assert len(issues) == 1
