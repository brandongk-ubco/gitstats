from gitstats.GithubConnection import GithubConnection
from datetime import datetime, timedelta
import os
import pytest


class TestGithubConnection:

    @pytest.mark.skip(
        reason="Relies on an external connection which is rate limited.")
    def test_can_connect(self):
        connection = GithubConnection("Test Group",
                                      os.environ.get("GITHUB_TOKEN"),
                                      "microsoft/vscode")
        end = datetime.now()
        start = end - timedelta(days=1)
        assert connection.get_repository() is not None
        assert connection.get_repository().get_commits(
            sha="master", since=start, until=end).totalCount >= 0
