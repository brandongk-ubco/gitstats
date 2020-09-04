from .dataframe import aggregate_list


class StatsCollector:

    def __init__(self, repository, start, end):
        self.repository = repository
        self.start = start
        self.end = end
        self._collect()

    def _collect(self):
        self.prs = self.repository.findPRsByDateRange(self.start, self.end)
        pr_ids = self.prs["id"].tolist()
        self.reviews = aggregate_list(
            [self.repository.getReviewsByPullRequestId(pr) for pr in pr_ids])
        self.commits = aggregate_list(
            [self.repository.getCommitsByPullRequestId(pr) for pr in pr_ids])
        self.comments = aggregate_list(
            [self.repository.getCommentsByPullRequestId(pr) for pr in pr_ids])

    def getPRs(self):
        return self.prs.copy()

    def getReviews(self):
        return self.reviews.copy()

    def getCommits(self):
        return self.commits.copy()

    def getComments(self):
        return self.comments.copy()
