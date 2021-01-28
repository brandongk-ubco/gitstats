import pandas as pd
from datetime import datetime
from github.GithubException import UnknownObjectException
import logging


class GithubAPIRepository:

    def __init__(self, repository, logger=None):
        self.repository = repository
        if logger is None:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logger

    def findPRsByDateRange(self, start, end):
        df = pd.DataFrame(columns=["id", "date", "assignee", "merged"])
        prs = self.repository.get_pulls(state="closed",
                                        sort="updated",
                                        direction="desc")

        self.logger.debug("Finding PRs between {} and {}".format(start, end))

        for pr in prs:
            self.logger.debug(
                "Inspecting PR {}, closed at {}, last updated at {}".format(
                    pr.number, pr.closed_at, pr.updated_at))
            labels = [str(i.name).lower().strip() for i in pr.labels]

            if "gitstats-ignore" in labels:
                self.logger.debug("PR {} labelled as Ignore".format(pr.number))
                continue

            if pr.closed_at is None or pr.closed_at > end:
                self.logger.debug("PR {} closed after end date {}".format(
                    pr.number, end))
                continue
            if pr.updated_at < start:
                self.logger.debug(
                    "PR {} last updated before start date {}".format(
                        pr.number, start))
                break

            self.logger.debug("Appending PR {}".format(pr.number))

            df = df.append(
                {
                    "id": pr.number,
                    "date": pr.closed_at,
                    "assignee": "" if pr.assignee is None else pr.assignee.name,
                    "merged": pr.merged
                },
                ignore_index=True)

        return df

    def getById(self, id):
        self.logger.debug("Finding PR {} by ID".format(id))
        return self.repository.get_pull(id)

    def getReviewsByPullRequestId(self, id):
        pr = self.getById(id)

        df = pd.DataFrame(columns=["pr", "id", "state", "date"])
        reviews = pr.get_reviews()
        self.logger.debug("Finding Reviews for PR {}".format(id))
        for review in reviews:
            self.logger.debug("Found Review {} for PR {}".format(review.id, id))
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
        self.logger.debug("Finding commits for PR {}".format(id))

        for commit in commits:
            self.logger.debug("Found commit {} for PR {}".format(
                commit.sha, id))

            if len(commit.parents) > 1:
                self.logger.debug(
                    "Commit {} in PR {} has multiple parents, ignoring".format(
                        commit.sha, id))
                continue

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

        self.logger.debug("Finding comments for PR {}".format(id))

        reviews = pr.get_reviews()
        for review in reviews:
            self.logger.debug("Found review {} for PR {}".format(review.id, id))
            df = df.append(
                {
                    "pr":
                        int(pr.number),
                    "date":
                        review.submitted_at,
                    "user":
                        review.user.name
                        if review.user.name else review.user.login,
                    "id":
                        review.id,
                    "type":
                        "review"
                },
                ignore_index=True)

        comments = pr.get_review_comments()
        for comment in comments:
            self.logger.debug("Found review comment {} for PR {}".format(
                comment.id, id))
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
            self.logger.debug("Found issue comment {} for PR {}".format(
                comment.id, id))
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

        self.logger.debug("Finding Issues between {} and {}".format(start, end))

        for issue in self.repository.get_issues(state="closed", since=start):

            self.logger.debug("Found issue {}, closed at {}".format(
                issue.number, issue.closed_at))

            try:
                self.repository.get_pull(issue.number)
                self.logger.debug("Issue {} is actually a Pull Request".format(
                    issue.number))
                continue
            except UnknownObjectException:
                pass

            if issue.closed_at > end:
                self.logger.debug("Issue {} closed after end date".format(
                    issue.number))
                continue

            self.logger.debug("Including issue {}".format(issue.number))
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
