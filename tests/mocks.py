from datetime import datetime, timedelta
from random import randint
import uuid
import pandas as pd
from github.GithubException import UnknownObjectException


class MockRepository:

    def __init__(self, prs=[], issues=[]):
        self.prs = prs
        self.issues = issues

    def get_pulls(self, *args, **kwargs):
        return self.prs

    def get_issues(self, *args, **kwargs):
        return self.issues

    def get_pull(self, id: int):
        pr = [p for p in self.prs if p.number == id]
        if len(pr) == 0:
            raise UnknownObjectException(status=404, data="PR does not exist")
        if len(pr) > 1:
            raise ValueError("Multiple PRs exist")
        return pr[0]


class MockPR:

    def __init__(self,
                 updated_at=None,
                 merged_at=None,
                 closed_at=None,
                 assignee=None,
                 merged=False,
                 number=None,
                 reviews=[],
                 commits=[],
                 issue_comments=[],
                 review_comments=[]):
        self.updated_at = updated_at if updated_at is not None else datetime.now(
        )
        self.merged_at = merged_at if merged_at is not None else datetime.now()
        self.closed_at = closed_at if closed_at is not None else datetime.now()
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
                 submitted_at: datetime = None,
                 user=None):
        self.id = id if id is not None else randint(1, 1e10)
        self.state = state
        self.submitted_at = submitted_at if submitted_at is not None else datetime.now(
        )
        self.user = user if user is not None else MockAuthor()


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

    def __init__(self,
                 author=None,
                 date=None,
                 stats=None,
                 sha=None,
                 parents=None):
        self.author = author if author is not None else MockAuthor()
        self.stats = stats if stats is not None else MockStats()
        self.sha = sha if sha is not None else uuid.uuid4().hex
        self.date = date if date is not None else datetime.now()
        self.parents = parents if parents is not None else []
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
        )
        self.user = user if user is not None else MockAuthor()
        self.id = id if id is not None else uuid.uuid4().hex


class MockStatsCollector:

    def __init__(self,
                 prs=None,
                 reviews=None,
                 comments=None,
                 commits=None,
                 issues=None,
                 users=None,
                 start=None,
                 end=None):
        self.prs = prs if prs is not None else pd.DataFrame(
            columns=["id", "date", "assignee", "merged"])
        self.reviews = reviews if reviews is not None else pd.DataFrame(
            columns=["pr", "id", "state", "date"])
        self.comments = comments if comments is not None else pd.DataFrame(
            columns=["pr", "date", "user", "type", "id"])
        self.commits = commits if commits is not None else pd.DataFrame(
            columns=[
                "pr", "user", "date", "date", "additions", "deletions", "id",
                "changes"
            ])
        self.issues = issues if issues is not None else pd.DataFrame(
            columns=["number", "date", "assignee", "labels"])
        self.users = users if users is not None else ["Bob", "Joan"]

        self.end = datetime.now() if end is None else end
        self.start = self.end - timedelta(days=7) if start is None else start

    def getPRs(self):
        return self.prs.copy()

    def getReviews(self):
        return self.reviews.copy()

    def getCommits(self):
        return self.commits.copy()

    def getComments(self):
        return self.comments.copy()

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def getIssues(self):
        return self.issues.copy()

    def get_users(self):
        return self.users


class MockStatsCalculator:

    def getContributionsByUserAndPR(self):
        return "contributions"

    def getEffortByUserFromContributions(self, contribuntions):
        return "effort"

    def get_start(self):
        return "start"

    def get_end(self):
        return "end"

    def getIssues(self):
        return ["issues"], ["excluded_issues"]

    def getTeamScore(self, issues, excluded_issues):
        return "teamscore"

    def getUsers(self):
        return ["Bob J.", "Joan B."]

    def getFinalScores(self, effort, team_score):
        return "finalscores"


class MockTemplate:

    def render(self, *args, **kwargs):
        return "-".join([k + str(v) for k, v in kwargs.items()])


class MockIssue:

    def __init__(self,
                 closed_at=None,
                 updated_at=None,
                 assignee=None,
                 state="closed",
                 number=None,
                 labels=[]):
        self.closed_at = closed_at if closed_at is not None else datetime.now()
        self.updated_at = updated_at if updated_at is not None else datetime.now(
        )
        self.assignee = assignee
        self.number = number if number is not None else randint(1, 1e10)
        self.labels = labels
        self.state = state
