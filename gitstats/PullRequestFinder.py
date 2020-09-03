import pandas as pd

class PullRequestFinder:

    def __init__(self, repository):
        self.repository = repository

    def find(self, start, end):
        df = pd.DataFrame()

        prs = self.repository.get_pulls(state="closed", sort="updated", direction="desc")
        
        for pr in prs:
            if pr.updated_at > end:
                continue
            if pr.updated_at < start:
                break

            df = df.append({
                "id": pr.number,
                "date": pr.updated_at,
                "assignee": "" if pr.assignee is None else pr.assignee.name,
                "merged": pr.merged
            }, ignore_index=True)

        return df
