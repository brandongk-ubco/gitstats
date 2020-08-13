from gitstats.GithubConnection import GithubConnection
from datetime import datetime, timezone, timedelta
import os

class TestGithubConnection:

    def test_can_connect(self):
        connection = GithubConnection("Test Group", os.environ.get("GITHUB_TOKEN"), "microsoft/vscode")
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=1)
        assert connection.repository is not None
        assert connection.repository.get_commits(sha=connection.branch.name, since=start, until=end).totalCount >= 0
