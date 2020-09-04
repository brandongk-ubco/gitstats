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


class MockReview:

    def __init__(self,
                 id: int = randint(1, 1e100),
                 state: str = "submitted",
                 submitted_at: datetime = datetime.now(timezone.utc)):
        self.id = id,
        self.state = state,
        self.submitted_at = submitted_at


class MockAuthor:

    def __init__(self, name=uuid.uuid4().hex):
        self.name = name


class MockStats:

    def __init__(self,
                 additions: int = randint(1, 1e100),
                 deletions: int = randint(1, 1e100)):
        self.additions = additions
        self.deletions = deletions
        self.total = self.additions + self.deletions


class MockCommit:

    def __init__(self,
                 author=MockAuthor(),
                 date=datetime.now(timezone.utc),
                 stats=MockStats(),
                 sha=uuid.uuid4().hex):
        self.author = author
        self.stats = stats
        self.sha = sha
        self.date = date
        self.raw_data = {
            "commit": {
                "author": {
                    "date": date.strftime("%Y-%m-%dT%H:%M:%SZ")
                }
            }
        }


class MockComment:

    def __init__(self,
                 updated_at=datetime.now(timezone.utc),
                 user=MockAuthor(),
                 id=uuid.uuid4().hex):
        self.updated_at = updated_at
        self.user = user
        self.id = id
