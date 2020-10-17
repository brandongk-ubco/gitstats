import pandas as pd
import pytest
from .fixtures import prs as prs_fixtures
from .fixtures import comments as comments_fixtures
from .fixtures import commits as commits_fixtures
from .fixtures import issues as issues_fixtures
from .mocks import MockStatsCollector
from gitstats import StatsCalculator
from datetime import datetime, timedelta
from backports.datetime_fromisoformat import MonkeyPatch
MonkeyPatch.patch_fromisoformat()


class TestStatsCalculator:

    def test_all_empty(self):
        collector = MockStatsCollector()
        calculator = StatsCalculator(collector)

        assert len(calculator.getUsers()) == 0
        assert len(calculator.getPRsByAssignee()) == 0
        assert len(calculator.getCommentsByUser()) == 0
        assert len(calculator.getCommentsByUserAndPR()) == 0
        assert len(calculator.getCommitsByUser()) == 0
        assert len(calculator.getCommitsByUserAndPR()) == 0
        assert len(calculator.getContributionsByUserAndPR()) == 0

    def test_prs_with_assignees(self):

        collector = MockStatsCollector(prs=prs_fixtures)
        calculator = StatsCalculator(collector)

        PRsByAssignee = calculator.getPRsByAssignee()
        assert len(calculator.getUsers()) == 2
        assert "Bob" in calculator.getUsers()
        assert "Joan" in calculator.getUsers()
        assert len(PRsByAssignee) == 2
        assert PRsByAssignee[PRsByAssignee["assignee"] ==
                             "Bob"]["assigned"].iloc[0] == 2
        assert PRsByAssignee[PRsByAssignee["assignee"] ==
                             "Joan"]["assigned"].iloc[0] == 1

        CommentsByUser = calculator.getCommentsByUser()
        assert len(calculator.getCommentsByUser()) == 2
        assert CommentsByUser[CommentsByUser["user"] ==
                              "Bob"]["comments"].iloc[0] == 0
        assert CommentsByUser[CommentsByUser["user"] ==
                              "Joan"]["comments"].iloc[0] == 0

        CommitsByUser = calculator.getCommitsByUser()
        assert len(CommitsByUser) == 2
        assert CommitsByUser[CommitsByUser["user"] ==
                             "Bob"]["commits"].iloc[0] == 0
        assert CommitsByUser[CommitsByUser["user"] ==
                             "Joan"]["commits"].iloc[0] == 0

        assert len(calculator.getCommentsByUserAndPR()) == 4
        assert len(calculator.getCommitsByUserAndPR()) == 4
        assert len(calculator.getContributionsByUserAndPR()) == 4

    def test_prs_with_comments(self):
        collector = MockStatsCollector(prs=prs_fixtures,
                                       comments=comments_fixtures)
        calculator = StatsCalculator(collector)

        PRsByAssignee = calculator.getPRsByAssignee()
        assert len(PRsByAssignee) == 2
        assert PRsByAssignee[PRsByAssignee["assignee"] ==
                             "Bob"]["assigned"].iloc[0] == 2
        assert PRsByAssignee[PRsByAssignee["assignee"] ==
                             "Joan"]["assigned"].iloc[0] == 1

        CommentsByUser = calculator.getCommentsByUser()
        assert len(CommentsByUser) == 2
        assert CommentsByUser[CommentsByUser["user"] ==
                              "Bob"]["comments"].iloc[0] == 1
        assert CommentsByUser[CommentsByUser["user"] ==
                              "Joan"]["comments"].iloc[0] == 0
        assert len(calculator.getCommitsByUser()) == 2
        assert len(calculator.getCommentsByUserAndPR()) == 4
        assert len(calculator.getCommitsByUserAndPR()) == 4
        assert len(calculator.getContributionsByUserAndPR()) == 4

    def test_prs_with_comments_and_commits(self):
        collector = MockStatsCollector(prs=prs_fixtures,
                                       comments=comments_fixtures,
                                       commits=commits_fixtures)
        calculator = StatsCalculator(collector)

        PRsByAssignee = calculator.getPRsByAssignee()
        assert len(PRsByAssignee) == 2
        assert PRsByAssignee[PRsByAssignee["assignee"] ==
                             "Bob"]["assigned"].iloc[0] == 2
        assert PRsByAssignee[PRsByAssignee["assignee"] ==
                             "Joan"]["assigned"].iloc[0] == 1

        CommentsByUser = calculator.getCommentsByUser()
        assert len(CommentsByUser) == 2
        assert CommentsByUser[CommentsByUser["user"] ==
                              "Bob"]["comments"].iloc[0] == 1
        assert CommentsByUser[CommentsByUser["user"] ==
                              "Joan"]["comments"].iloc[0] == 0
        CommitsByUser = calculator.getCommitsByUser()
        assert len(CommitsByUser) == 2
        assert CommitsByUser[CommitsByUser["user"] ==
                             "Bob"]["commits"].iloc[0] == 1
        assert CommitsByUser[CommitsByUser["user"] ==
                             "Joan"]["commits"].iloc[0] == 0
        assert len(calculator.getCommentsByUserAndPR()) == 4
        assert len(calculator.getCommitsByUserAndPR()) == 4

        ContributionsByUserAndPR = calculator.getContributionsByUserAndPR()
        assert len(ContributionsByUserAndPR) == 4
        bob_0 = ContributionsByUserAndPR[
            (ContributionsByUserAndPR["user"] == "Bob") &
            (ContributionsByUserAndPR["pr"] == 0)]
        bob_1 = ContributionsByUserAndPR[
            (ContributionsByUserAndPR["user"] == "Bob") &
            (ContributionsByUserAndPR["pr"] == 1)]
        joan_0 = ContributionsByUserAndPR[
            (ContributionsByUserAndPR["user"] == "Joan") &
            (ContributionsByUserAndPR["pr"] == 0)]
        joan_1 = ContributionsByUserAndPR[
            (ContributionsByUserAndPR["user"] == "Joan") &
            (ContributionsByUserAndPR["pr"] == 1)]
        assert bob_0["contributed"].iloc[0]
        assert not bob_1["contributed"].iloc[0]
        assert not joan_0["contributed"].iloc[0]
        assert not joan_1["contributed"].iloc[0]

    def test_effort_with_comments_and_commits(self):
        collector = MockStatsCollector(prs=prs_fixtures,
                                       comments=comments_fixtures,
                                       commits=commits_fixtures)
        calculator = StatsCalculator(collector)

        contributions = calculator.getContributionsByUserAndPR()

        effort = calculator.getEffortByUserFromContributions(contributions)
        assert effort[effort["user"] == "Bob"]["effort"].iloc[0] == 100.0
        assert effort[effort["user"] == "Joan"]["effort"].iloc[0] == 0.0

    def test_effort_with_only_comments(self):
        collector = MockStatsCollector(prs=prs_fixtures,
                                       comments=comments_fixtures)
        calculator = StatsCalculator(collector)

        contributions = calculator.getContributionsByUserAndPR()

        effort = calculator.getEffortByUserFromContributions(contributions)
        assert effort[effort["user"] == "Bob"]["effort"].iloc[0] == 100.0
        assert effort[effort["user"] == "Joan"]["effort"].iloc[0] == 0.0

    def test_get_start(self):
        collector = MockStatsCollector()
        calculator = StatsCalculator(collector)
        assert calculator.get_start() - collector.get_start() < timedelta(
            seconds=1)

    def test_get_end(self):
        collector = MockStatsCollector()
        calculator = StatsCalculator(collector)
        assert calculator.get_end() - collector.get_end() < timedelta(seconds=1)

    def test_issues(self):
        collector = MockStatsCollector(issues=issues_fixtures)
        calculator = StatsCalculator(collector)
        issues, excluded_issues = calculator.getIssues()
        assert len(issues) == 1
        assert len(excluded_issues) == 4

    def test_team_score_two_users_one_issue(self):
        users = ["Bob", "Joan"]

        collector = MockStatsCollector(issues=issues_fixtures)
        calculator = StatsCalculator(collector)
        issues, excluded_issues = calculator.getIssues()

        assert calculator.getExpectedIssuesPerUser() - 4 < 0.01
        team_score = calculator.getTeamScore(users, issues)
        assert team_score == 0.25

    def test_expected_issues_one_week(self):
        collector = MockStatsCollector()
        calculator = StatsCalculator(collector)
        expected_issues = calculator.getExpectedIssuesPerUser()

        assert expected_issues - 2 < 0.01

    def test_expected_issues_two_weeks(self):

        end = datetime.now()
        start = datetime.now() - timedelta(days=14)
        collector = MockStatsCollector(start=start, end=end)
        calculator = StatsCalculator(collector)
        expected_issues = calculator.getExpectedIssuesPerUser()

        assert expected_issues - 4 < 0.01

    def test_expected_issues_five_days(self):
        start = datetime.fromisoformat('2020-09-18T10:30')
        end = datetime.fromisoformat('2020-09-23T10:30')

        collector = MockStatsCollector(start=start, end=end)
        calculator = StatsCalculator(collector)
        expected_issues = calculator.getExpectedIssuesPerUser()

        assert expected_issues - 1.42 < 0.01

    def test_team_score_one_user_one_issue_two_weeks(self):
        users = ["Bob"]

        end = datetime.now()
        start = datetime.now() - timedelta(days=14)
        collector = MockStatsCollector(start=start,
                                       end=end,
                                       issues=issues_fixtures)
        calculator = StatsCalculator(collector)
        issues, excluded_issues = calculator.getIssues()

        assert calculator.getExpectedIssuesPerUser() - 4 < 0.01

        team_score = calculator.getTeamScore(users, issues)
        assert team_score - 0.25 < 0.01

    def test_team_score_two_users_one_issue_two_weeks(self):
        users = ["Bob", "Joan"]

        end = datetime.now()
        start = datetime.now() - timedelta(days=14)
        collector = MockStatsCollector(start=start,
                                       end=end,
                                       issues=issues_fixtures)
        calculator = StatsCalculator(collector)
        issues, excluded_issues = calculator.getIssues()

        assert calculator.getExpectedIssuesPerUser() - 8 < 0.01

        team_score = calculator.getTeamScore(users, issues)
        assert team_score - 0.125 < 0.01

    def test_team_score_one_user_one_issue(self):
        users = ["Bob"]

        collector = MockStatsCollector(issues=issues_fixtures)
        calculator = StatsCalculator(collector)
        issues, excluded_issues = calculator.getIssues()

        team_score = calculator.getTeamScore(users, issues)
        assert team_score == 0.50

    def test_team_score_one_user_three_issues(self):
        users = ["Bob"]

        mock_issues = issues_fixtures.copy(deep=True)
        mock_issues = mock_issues.append(
            {
                "number": 20,
                "date": datetime.now(),
                "assignee": "Bob",
                "labels": ["chore"]
            },
            ignore_index=True)
        mock_issues = mock_issues.append(
            {
                "number": 21,
                "date": datetime.now(),
                "assignee": "Bob",
                "labels": ["exploration"]
            },
            ignore_index=True)

        collector = MockStatsCollector(issues=mock_issues)
        calculator = StatsCalculator(collector)
        issues, excluded_issues = calculator.getIssues()

        team_score = calculator.getTeamScore(users, issues)
        assert team_score == 1.50

    def test_team_score_one_user_four_issues(self):
        users = ["Bob"]

        mock_issues = issues_fixtures.copy(deep=True)
        mock_issues = mock_issues.append(
            {
                "number": 20,
                "date": datetime.now(),
                "assignee": "Bob",
                "labels": ["chore"]
            },
            ignore_index=True)
        mock_issues = mock_issues.append(
            {
                "number": 21,
                "date": datetime.now(),
                "assignee": "Bob",
                "labels": ["exploration"]
            },
            ignore_index=True)
        mock_issues = mock_issues.append(
            {
                "number": 22,
                "date": datetime.now(),
                "assignee": "Bob",
                "labels": ["task"]
            },
            ignore_index=True)

        collector = MockStatsCollector(issues=mock_issues)
        calculator = StatsCalculator(collector)
        issues, excluded_issues = calculator.getIssues()

        team_score = calculator.getTeamScore(users, issues)
        assert team_score == 1.50

    def test_team_score_no_users(self):
        users = []

        collector = MockStatsCollector()
        calculator = StatsCalculator(collector)
        issues, excluded_issues = calculator.getIssues()

        team_score = calculator.getTeamScore(users, issues)
        assert team_score == 0.00

    @pytest.mark.parametrize("test_more,test_input,expected", [
        (5000, 1000, 83.35),
        (5000, 500, 68.77),
        (5000, 250, 50.78),
        (5000, 100, 28.26),
        (5000, 50, 16.15),
        (5000, 0, 0),
        (10000, 1000, 83.35),
        (10000, 500, 68.77),
        (10000, 250, 50.78),
        (10000, 100, 28.26),
        (10000, 50, 16.15),
        (10000, 0, 0),
    ])
    def test_nonlinear_changes(self, test_more, test_input, expected):

        contributions = pd.DataFrame.from_records([{
            "user": "Bob",
            "pr": 0,
            "commits": 0,
            "changes": test_more,
            "comments": 0,
            "contributed": True
        }, {
            "user": "Joan",
            "pr": 0,
            "commits": 0,
            "changes": test_input,
            "comments": 0,
            "contributed": True
        }])

        effort = StatsCalculator(None).getEffortByUserFromContributions(
            contributions)

        assert abs(effort[effort["user"] == "Bob"]["changes"].iloc[0] -
                   100) < 0.01
        assert abs(effort[effort["user"] == "Joan"]["changes"].iloc[0] -
                   expected) < 0.01
