from gitstats.MultiGithubAPIRepository import MultiGithubAPIRepository
from gitstats.GithubAPIRepository import GithubAPIRepository
from datetime import datetime, timedelta
import pytest
from .mocks import MockRepository, MockPR, MockReview, MockCommit, MockComment, MockIssue, MockLabel


class TestGithubAPIRepository:

    def _mock_pr_response(self, expected_prs=[]):
        finder = MultiGithubAPIRepository()
        finder.repositories = [
            self._mock_single_pr_response(e) for e in expected_prs
        ]
        return finder

    def _mock_issue_response(self, expected_issues=[]):
        finder = MultiGithubAPIRepository()
        finder.repositories = [
            self._mock_single_issue_response(e) for e in expected_issues
        ]
        return finder

    def _mock_single_pr_response(self, expected_prs=[]):
        repository = MockRepository(expected_prs)
        finder = GithubAPIRepository(repository)
        return finder

    def _mock_single_issue_response(self, expected_issues=[]):
        repository = MockRepository(issues=expected_issues)
        finder = GithubAPIRepository(repository)
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
        expected_prs = [[MockPR()], [MockPR()]]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert prs["id"][0].startswith("0-")
        assert prs["id"][1].startswith("1-")
        assert len(prs) == len(expected_prs)

    @pytest.mark.findPRsByDateRange
    def test_not_merged(self):
        expected_prs = [[MockPR()], [MockPR()]]
        expected_prs[0][0].closed_at = None
        expected_prs[1][0].closed_at = None
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 0

    @pytest.mark.findPRsByDateRange
    def test_two_prs(self):
        expected_prs = [[MockPR(), MockPR()], [MockPR(), MockPR()]]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert prs["id"][0].startswith("0-")
        assert prs["id"][1].startswith("0-")
        assert prs["id"][2].startswith("1-")
        assert prs["id"][3].startswith("1-")
        assert len(prs) == 4

    @pytest.mark.findPRsByDateRange
    def test_prs_start_at_right_date(self):
        expected_prs = [[
            MockPR(),
            MockPR(closed_at=datetime.now() - timedelta(days=10))
        ], [MockPR(),
            MockPR(closed_at=datetime.now() - timedelta(days=10))]]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert prs["id"][0].startswith("0-")
        assert prs["id"][1].startswith("1-")
        assert len(prs) == 2

    @pytest.mark.findPRsByDateRange
    def test_prs_skip_after_end_date(self):
        expected_prs = [[
            MockPR(closed_at=datetime.now() + timedelta(days=1)),
            MockPR()
        ], [MockPR(closed_at=datetime.now() + timedelta(days=1)),
            MockPR()]]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert prs["id"][0].startswith("0-")
        assert prs["id"][1].startswith("1-")
        assert len(prs) == 2

    @pytest.mark.findPRsByDateRange
    def test_ignores_one_pr(self):
        expected_prs = [[MockPR(labels=[MockLabel("gitstats-ignore")])],
                        [MockPR(labels=[MockLabel("gitstats-ignore")])]]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert len(prs) == 0

    @pytest.mark.findPRsByDateRange
    def test_ignores_one_pr_but_not_both(self):
        expected_prs = [[
            MockPR(labels=[MockLabel("gitstats-ignore")]),
            MockPR(MockLabel("do-not-ignore"))
        ],
                        [
                            MockPR(labels=[MockLabel("gitstats-ignore")]),
                            MockPR(MockLabel("do-not-ignore"))
                        ]]
        finder = self._mock_pr_response(expected_prs)
        end = datetime.now()
        start = end - timedelta(days=7)
        prs = finder.findPRsByDateRange(start, end)
        assert prs["id"][0].startswith("0-")
        assert prs["id"][1].startswith("1-")
        assert len(prs) == 2

    @pytest.mark.getById
    def test_returns_get_pull_response(self):
        expected_prs = [[MockPR()], [MockPR()]]
        finder = self._mock_pr_response(expected_prs)
        assert finder.getById("0-{}".format(
            expected_prs[0][0].number)) == expected_prs[0][0]
        assert finder.getById("1-{}".format(
            expected_prs[1][0].number)) == expected_prs[1][0]

    @pytest.mark.getReviewsByPullRequestId
    def test_returns_reviews(self):
        expected_reviews = [[MockReview(), MockReview()],
                            [MockReview(), MockReview()]]
        prs = [[MockPR(reviews=expected_reviews[0])],
               [MockPR(reviews=expected_reviews[1])]]
        finder = self._mock_pr_response(prs)

        # Check the first repository
        reviews = finder.getReviewsByPullRequestId("0-{}".format(
            prs[0][0].number))
        for pr_id in reviews["pr"]:
            assert pr_id.startswith("0-")
        assert len(reviews) == len(expected_reviews[0])

        # Check the second repository
        reviews = finder.getReviewsByPullRequestId("1-{}".format(
            prs[1][0].number))
        for pr_id in reviews["pr"]:
            assert pr_id.startswith("1-")
        assert len(reviews) == len(expected_reviews[1])

    @pytest.mark.getCommitsByPullRequestId
    def test_returns_commits(self):
        expected_commits = [[MockCommit(), MockCommit()],
                            [MockCommit(), MockCommit()]]
        prs = [[MockPR(commits=expected_commits[0])],
               [MockPR(commits=expected_commits[1])]]
        finder = self._mock_pr_response(prs)

        # Check the first repository
        commits = finder.getCommitsByPullRequestId("0-{}".format(
            prs[0][0].number))
        for pr_id in commits["pr"]:
            assert pr_id.startswith("0-")
        assert len(commits) == len(expected_commits[0])
        for i in range(0, len(commits)):
            actual_date = commits["date"][i]
            expected_date = expected_commits[0][i].date
            assert abs(actual_date - expected_date) < timedelta(seconds=1)

        # Check the second repository
        commits = finder.getCommitsByPullRequestId("1-{}".format(
            prs[1][0].number))
        for pr_id in commits["pr"]:
            assert pr_id.startswith("1-")
        assert len(commits) == len(expected_commits[1])
        for i in range(0, len(commits)):
            actual_date = commits["date"][i]
            expected_date = expected_commits[1][i].date
            assert abs(actual_date - expected_date) < timedelta(seconds=1)

    # @pytest.mark.getCommitsByPullRequestId
    # def test_ignores_merge_commits(self):
    #     commit_1 = MockCommit()
    #     commit_2 = MockCommit()
    #     merge_commit = MockCommit(parents=[commit_1, commit_2])
    #     expected_commits = [commit_1, commit_2, merge_commit]
    #     pr = MockPR(commits=expected_commits)
    #     finder = self._mock_pr_response([pr])
    #     commits = finder.getCommitsByPullRequestId(pr.number)
    #     assert len(commits) == 2
    #     for i in range(0, len(commits)):
    #         actual_date = commits["date"][i]
    #         expected_date = expected_commits[i].date
    #         assert abs(actual_date - expected_date) < timedelta(seconds=1)

    # @pytest.mark.getCommentsByPullRequestId
    # def test_returns_comments(self):
    #     expected_review_comments = [MockComment(), MockComment()]
    #     expected_issue_comments = [MockComment(), MockComment()]
    #     pr = MockPR(issue_comments=expected_issue_comments,
    #                 review_comments=expected_review_comments)
    #     finder = self._mock_pr_response([pr])
    #     comments = finder.getCommentsByPullRequestId(pr.number)
    #     assert len(comments) == len(expected_review_comments) + len(
    #         expected_issue_comments)

    # @pytest.mark.findIssuesByDateRange
    # def test_no_issues(self):
    #     expected_issues = []
    #     finder = self._mock_issue_response(expected_issues)
    #     end = datetime.now()
    #     start = end - timedelta(days=7)
    #     prs = finder.findIssuesByDateRange(start, end)
    #     assert len(prs) == 0

    # @pytest.mark.findIssuesByDateRange
    # def test_one_issue(self):
    #     expected_issues = [MockIssue()]
    #     finder = self._mock_issue_response(expected_issues)
    #     end = datetime.now()
    #     start = end - timedelta(days=7)
    #     issues = finder.findIssuesByDateRange(start, end)
    #     assert len(issues) == len(expected_issues)

    # @pytest.mark.findIssuesByDateRange
    # def test_two_issues(self):
    #     expected_issues = [MockIssue(), MockIssue()]
    #     finder = self._mock_issue_response(expected_issues)
    #     end = datetime.now()
    #     start = end - timedelta(days=7)
    #     issues = finder.findIssuesByDateRange(start, end)
    #     assert len(issues) == 2

    # @pytest.mark.findIssuesByDateRange
    # def test_issues_start_at_right_date(self):
    #     expected_issues = [
    #         MockIssue(),
    #         MockIssue(closed_at=datetime.now() - timedelta(days=10))
    #     ]
    #     finder = self._mock_issue_response(expected_issues)
    #     end = datetime.now()
    #     start = end - timedelta(days=7)
    #     issues = finder.findIssuesByDateRange(start, end)
    #     assert len(issues) == 1

    # @pytest.mark.findIssuesByDateRange
    # def test_issues_skip_after_end_date(self):
    #     expected_issues = [
    #         MockIssue(closed_at=datetime.now() + timedelta(days=1)),
    #         MockIssue()
    #     ]
    #     finder = self._mock_issue_response(expected_issues)
    #     end = datetime.now()
    #     start = end - timedelta(days=7)
    #     issues = finder.findIssuesByDateRange(start, end)
    #     assert len(issues) == 1
