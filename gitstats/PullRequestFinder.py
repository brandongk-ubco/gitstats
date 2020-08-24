from . import GithubConnection
import pandas as pd

class PullRequestFinder:

    def __init__(self, connection: GithubConnection):
        self.connection = connection

    def find(self, start, end):
        pr_df = pd.DataFrame()

        prs = self.connection.repository.get_pulls(state="closed", sort="updated", direction="desc")

        if not prs:
            return pr_df

        for pr in prs:
            if pr.updated_at > end:
                continue
            if pr.updated_at < start:
                break
            pr_df = pr_df.append({
                "id": pr.number,
                "date": pr.updated_at,
                "assignee": "" if pr.assignee is None else pr.assignee.name,
                "merged": pr.merged
            }, ignore_index=True)

        return prs