import pandas as pd
from datetime import datetime


class PullRequestRepository:

    def __init__(self, repository):
        self.repository = repository

    def findPRsByDateRange(self, start, end):
        df = pd.DataFrame(columns=["id", "date", "assignee", "merged"])
        prs = self.repository.get_pulls(state="closed",
                                        sort="updated",
                                        direction="desc")

        for pr in prs:
            if pr.updated_at > end:
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
                    "user": commit.author.name,
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
                    "pr": int(pr.number),
                    "date": comment.updated_at,
                    "user": comment.user.name,
                    "id": comment.id,
                    "type": "review"
                },
                ignore_index=True)

        comments = pr.get_issue_comments()
        for comment in comments:
            df = df.append(
                {
                    "pr": int(pr.number),
                    "date": comment.updated_at,
                    "user": comment.user.name,
                    "id": comment.id,
                    "type": "issue"
                },
                ignore_index=True)

        return df
