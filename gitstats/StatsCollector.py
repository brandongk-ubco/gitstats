from .dataframe import aggregate_list
from datetime import datetime, timedelta
import pytz


class StatsCollector:

    @staticmethod
    def default_end(today=None):
        if today is None:
            today = datetime.utcnow().replace(tzinfo=pytz.UTC)
        tzoffset = datetime.utcnow() - datetime.now()
        today = today.replace(hour=0, minute=0, second=0,
                              microsecond=0) + tzoffset + timedelta(hours=10,
                                                                    minutes=30)
        if today.weekday() < 2:
            today = today - timedelta(weeks=1)
        return today - timedelta(days=today.weekday()) + timedelta(days=2)

    def default_start(self, end=None):
        if end is None:
            end = StatsCollector.default_end()
        return end - timedelta(weeks=self.weeks)

    def __init__(self, repository, start=None, end=None, weeks=1):
        self.repository = repository

        self.weeks = weeks

        if end is None:
            end = StatsCollector.default_end()
        if start is None:
            start = self.default_start(end)

        self.start = start
        self.end = end
        self._collect()

    def _collect(self):
        self.prs = self.repository.findPRsByDateRange(self.start, self.end)

        if len(self.prs) > 0:
            pr_ids = self.prs["id"].tolist()
        else:
            pr_ids = []
        self.reviews = aggregate_list(
            [self.repository.getReviewsByPullRequestId(pr) for pr in pr_ids],
            columns=["pr", "id", "state", "date"])
        self.commits = aggregate_list(
            [self.repository.getCommitsByPullRequestId(pr) for pr in pr_ids],
            columns=[
                "pr", "user", "date", "additions", "deletions", "id", "changes"
            ])
        self.comments = aggregate_list(
            [self.repository.getCommentsByPullRequestId(pr) for pr in pr_ids],
            columns=["pr", "date", "user", "id", "type"])

        self.issues = self.repository.findIssuesByDateRange(
            self.start, self.end)

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def getPRs(self):
        return self.prs.copy()

    def getIssues(self):
        return self.issues.copy()

    def getReviews(self):
        return self.reviews.copy()

    def getCommits(self):
        return self.commits.copy()

    def getComments(self):
        return self.comments.copy()
