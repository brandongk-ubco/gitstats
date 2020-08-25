from gitstats.PullRequestFinder import PullRequestFinder
from datetime import datetime, timezone, timedelta
import json
import os
import pathlib
from github.PullRequest import PullRequest

current_file = pathlib.Path(__file__).parent.absolute()

class MockGithubConnection:    
    def __init__(self, repository):
        self.repository = repository

    def get_repository(self):
        return self.repository

class MockRepository:

    def __init__(self, prs=[]):
        self.prs = prs

    def get_pulls(self, *args, **kwargs):
        return self.prs

class TestPullRequestFinder:

    def _mock_pr_response(self, expected_prs=[]):
        connection = MockGithubConnection(MockRepository(expected_prs))
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=7)
        finder = PullRequestFinder(connection)
        return finder.find(start, end)

    def test_no_prs(self):
        prs = self._mock_pr_response()
        assert len(prs) == 0

    def test_some_prs(self):
        expected_prs = [PullRequest(requester="", headers=[], attributes=[], completed="")]
        prs = self._mock_pr_response(expected_prs)
        assert len(prs) == len(expected_prs)
