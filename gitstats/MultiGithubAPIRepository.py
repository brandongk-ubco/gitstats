import pandas as pd
from .GithubAPIRepository import GithubAPIRepository


class MultiGithubAPIRepository:

    def __init__(self, repositories):
        self.repositories = [GithubAPIRepository(r) for r in repositories]

    def findPRsByDateRange(self, start, end):
        df = pd.DataFrame(columns=["id", "date", "assignee", "merged"])
        for i, repository in enumerate(self.repositories):
            repository_df = repository.findPRsByDateRange(start, end)
            repository_df["id"] = repository_df["id"].apply(
                lambda id: "{}-{}".format(i, id))
            df = df.append(repository_df, ignore_index=True)
        return df

    def getReviewsByPullRequestId(self, id):
        repository, pr_id = id.split("-")
        return self.repositories[int(repository)].getReviewsByPullRequestId(
            pr_id)

    def getCommitsByPullRequestId(self, id):
        repository, pr_id = id.split("-")
        return self.repositories[int(repository)].getCommitsByPullRequestId(
            pr_id)

    def getCommentsByPullRequestId(self, id):
        repository, pr_id = id.split("-")
        return self.repositories[int(repository)].getCommentsByPullRequestId(
            pr_id)

    def findIssuesByDateRange(self, start, end):
        df = pd.DataFrame(columns=["number", "date", "assignee", "labels"])
        for i, repository in enumerate(self.repositories):
            repository_df = repository.findIssuesByDateRange(id)
            repository_df["id"] = repository_df["id"].apply(
                lambda id: "{}-{}".format(i, id))
            df = df.append(repository_df, ignore_index=True)
        return df
