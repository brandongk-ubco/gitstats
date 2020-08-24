from gitstats.PullRequestFinder import PullRequestFinder
from datetime import datetime, timezone, timedelta
import os

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

    def test_no_prs(self):
        connection = MockGithubConnection(MockRepository())
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=7)
        finder = PullRequestFinder(connection)
        prs = finder.find(start, end)
        assert len(prs) == 0
