import pandas as pd
from .GithubAPIRepository import GithubAPIRepository


class MultiGithubAPIRepository:

    def __init__(self, repositories=[]):
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
        reviews_df = self.repositories[int(
            repository)].getReviewsByPullRequestId(int(pr_id))
        reviews_df["pr"] = reviews_df["pr"].apply(
            lambda id: "{}-{}".format(repository, pr_id))
        return reviews_df

    def getCommitsByPullRequestId(self, id):
        repository, pr_id = id.split("-")
        commits_df = self.repositories[int(
            repository)].getCommitsByPullRequestId(int(pr_id))
        commits_df["pr"] = commits_df["pr"].apply(
            lambda id: "{}-{}".format(repository, pr_id))
        return commits_df

    def getCommentsByPullRequestId(self, id):
        repository, pr_id = id.split("-")
        comments_df = self.repositories[int(
            repository)].getCommentsByPullRequestId(int(pr_id))
        comments_df["pr"] = comments_df["pr"].apply(
            lambda id: "{}-{}".format(repository, pr_id))
        return comments_df

    def findIssuesByDateRange(self, start, end):
        df = pd.DataFrame(columns=["number", "date", "assignee", "labels"])
        for i, repository in enumerate(self.repositories):
            repository_df = repository.findIssuesByDateRange(start, end)
            repository_df["number"] = repository_df["number"].apply(
                lambda id: "{}-{}".format(i, id))
            df = df.append(repository_df, ignore_index=True)
        return df

    def getById(self, id):
        repository, pr_id = id.split("-")
        return self.repositories[int(repository)].getById(int(pr_id))
