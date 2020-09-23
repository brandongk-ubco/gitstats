import pandas as pd
from datetime import datetime
from github.GithubException import UnknownObjectException


class GithubAPIRepository:

    def __init__(self, repository):
        self.repository = repository

    def findPRsByDateRange(self, start, end):
        df = pd.DataFrame(columns=["id", "date", "assignee", "merged"])
        prs = self.repository.get_pulls(state="closed",
                                        sort="merged",
                                        direction="desc")

        for pr in prs:
            if pr.merged_at is None or pr.merged_at > end:
                continue
            if pr.updated_at < start:
                break

            df = df.append(
                {
                    "id": pr.number,
                    "date": pr.updated_at,
                    "assignee": "" if pr.assignee is None else pr.assignee.name,
                    "merged": pr.merged
                },
                ignore_index=True)

        return df

    def getById(self, id):
        return self.repository.get_pull(id)

    def getReviewsByPullRequestId(self, id):
        pr = self.getById(id)

        df = pd.DataFrame(columns=["pr", "id", "state", "date"])
        reviews = pr.get_reviews()
        for review in reviews:
            df = df.append(
                {
                    "pr": int(pr.number),
                    "id": review.id,
                    "state": review.state,
                    "date": review.submitted_at
                },
                ignore_index=True)
        return df

    @staticmethod
    def resolve_author(commit):
        if commit.author is None:
            return commit.commit.raw_data["author"]["name"]
        else:
            return commit.author.name if commit.author.name else commit.author.login

    def getCommitsByPullRequestId(self, id):
        pr = self.getById(id)

        df = pd.DataFrame(columns=[
            "pr", "user", "date", "additions", "deletions", "id", "changes"
        ])

        commits = pr.get_commits()
        for commit in commits:

            date = datetime.strptime(
                commit.raw_data["commit"]["author"]["date"],
                "%Y-%m-%dT%H:%M:%SZ")
            df = df.append(
                {
                    "pr": int(pr.number),
                    "user": GithubAPIRepository.resolve_author(commit),
                    "date": date,
                    "additions": commit.stats.additions,
                    "deletions": commit.stats.deletions,
                    "id": commit.sha,
                    "changes": commit.stats.total
                },
                ignore_index=True)

        return df

    def getCommentsByPullRequestId(self, id):

        pr = self.getById(id)

        df = pd.DataFrame(columns=["pr", "date", "user", "id", "type"])

        comments = pr.get_review_comments()
        for comment in comments:
            df = df.append(
                {
                    "pr":
                        int(pr.number),
                    "date":
                        comment.updated_at,
                    "user":
                        comment.user.name
                        if comment.user.name else comment.user.login,
                    "id":
                        comment.id,
                    "type":
                        "review"
                },
                ignore_index=True)

        comments = pr.get_issue_comments()
        for comment in comments:
            df = df.append(
                {
                    "pr":
                        int(pr.number),
                    "date":
                        comment.updated_at,
                    "user":
                        comment.user.name
                        if comment.user.name else comment.user.login,
                    "id":
                        comment.id,
                    "type":
                        "issue"
                },
                ignore_index=True)

        return df

    def findIssuesByDateRange(self, start, end):
        df = pd.DataFrame(columns=["number", "date", "assignee", "labels"])
        issues = []
        for issue in self.repository.get_issues(state="closed",
                                                sort="closed",
                                                direction="desc"):
            if issue.closed_at > end:
                continue
            if issue.updated_at < start:
                break

            try:
                self.repository.get_pull(issue.number)
            except UnknownObjectException:
                issues.append(issue)

        for issue in issues:
            df = df.append(
                {
                    "number":
                        issue.number,
                    "date":
                        issue.closed_at,
                    "assignee":
                        "" if issue.assignee is None else issue.assignee.name,
                    "labels":
                        [str(i.name).lower().strip() for i in issue.labels]
                },
                ignore_index=True)

        return df
