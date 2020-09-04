class StatsCalculator:

    def __init__(self, statsCollector):
        self.statsCollecter = statsCollector

    def getPRsByAssignee(self):
        return self.statsCollecter.getPRs().groupby(['assignee']).agg({
            'id': 'count'
        }).reset_index().rename(columns={
            'id': 'assigned'
        }).sort_values(by="assigned", ascending=False)

    def getCommentsByUser(self):
        return self.statsCollecter.getComments().groupby(['user']).agg({
            'id': 'count'
        }).reset_index().rename(columns={
            'id': 'comments'
        }).sort_values(by="comments", ascending=False).copy()

    def getCommitsByUser(self):
        return self.statsCollecter.getCommits().groupby(['user']).agg({
            'id': 'count',
            'additions': 'sum',
            'deletions': 'sum',
            'changes': 'sum'
        }).reset_index().rename(columns={
            'id': 'commits'
        }).sort_values(by="commits", ascending=False).copy()

    def getCommentsByUserAndPR(self):
        return self.statsCollecter.getComments().groupby(['user', 'pr']).agg({
            'id': 'count'
        }).reset_index().rename(columns={'id': 'comments'})

    def getCommitsByUserAndPR(self):
        return self.statsCollecter.getCommits().groupby(['user', 'pr']).agg({
            'id': 'count',
            'additions': 'sum',
            'deletions': 'sum',
            'changes': 'sum'
        }).reset_index().rename(columns={'id': 'commits'})

    def getContributionsByUserAndPR(self):

        aggregated = self.statsCollecter.getPRs().merge(
            self.getCommitsByUserAndPR(),
            how="left",
            left_on="id",
            right_on="pr",
            suffixes=("", "_commits")).sort_values(by=["id", "user"])

        aggregated = aggregated.merge(
            self.getCommentsByUserAndPR(),
            how="left",
            left_on=["id", "user"],
            right_on=["pr", "user"],
            suffixes=("", "_comments")).sort_values(by=["id", "user"])

        aggregated = aggregated.fillna(0)
        aggregated.drop(aggregated[aggregated['user'] == 0].index, inplace=True)

        aggregated["contributions"] = aggregated["commits"] + aggregated[
            "changes"] + aggregated["comments"]
        aggregated["contributed"] = aggregated["contributions"] > 0

        return aggregated
