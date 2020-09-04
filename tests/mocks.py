from datetime import datetime, timezone
from random import randint
import uuid


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
                 updated_at=None,
                 assignee=None,
                 merged=False,
                 number=None,
                 reviews=[],
                 commits=[],
                 issue_comments=[],
                 review_comments=[]):
        self.updated_at = updated_at if updated_at is not None else datetime.now(
            timezone.utc)
        self.assignee = assignee
        self.merged = merged
        self.number = number if number is not None else randint(1, 1e10)
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


class MockReview:

    def __init__(self,
                 id: int = None,
                 state: str = "submitted",
                 submitted_at: datetime = None):
        self.id = id if id is not None else randint(1, 1e10)
        self.state = state
        self.submitted_at = submitted_at if submitted_at is not None else datetime.now(
            timezone.utc)


class MockAuthor:

    def __init__(self, name=None):
        self.name = name if name is not None else uuid.uuid4().hex


class MockStats:

    def __init__(self, additions: int = None, deletions: int = None):
        self.additions = additions if additions is not None else randint(
            1, 1e10)
        self.deletions = deletions if deletions is not None else randint(
            1, 1e10)
        self.total = self.additions + self.deletions


class MockCommit:

    def __init__(self, author=None, date=None, stats=None, sha=None):
        self.author = author if author is not None else MockAuthor()
        self.stats = stats if stats is not None else MockStats()
        self.sha = sha if sha is not None else uuid.uuid4().hex
        self.date = date if date is not None else datetime.now(timezone.utc)
        self.raw_data = {
            "commit": {
                "author": {
                    "date": self.date.strftime("%Y-%m-%dT%H:%M:%SZ")
                }
            }
        }


class MockComment:

    def __init__(self, updated_at=None, user=None, id=None):
        self.updated_at = updated_at if updated_at is not None else datetime.now(
            timezone.utc)
        self.user = user if user is not None else MockAuthor()
        self.id = id if id is not None else uuid.uuid4().hex
