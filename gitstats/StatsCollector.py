from .dataframe import aggregate_list


class StatsCollector:

    def __init__(self, repository, start, end, excluded_users=[]):
        self.repository = repository

        self.start = start
        self.end = end
        self.excluded_users = excluded_users
        self._collect()
        self._filter()

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

    def _filter(self):
        self.commits = self.commits[~self.commits.user.isin(self.excluded_users
                                                           )]
        self.comments = self.comments[~self.comments.user.isin(self.
                                                               excluded_users)]
        self.prs[self.prs.assignee.isin(self.excluded_users)]["assignee"] = ""
        self.issues[self.issues.assignee.isin(
            self.excluded_users)]["assignee"] = ""

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
