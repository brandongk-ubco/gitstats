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

    def get_prs(self):
        return self.prs

    def get_reviews(self):
        return self.reviews

    def get_commits(self):
        return self.commits

    def get_comments(self):
        return self.comments
