class AbsoluteEffortWithBonusNormalizer:

    def __init__(self,
                 expected_changes,
                 expected_commits,
                 expected_tasks_per_user,
                 bonus_slope=0.25,
                 maximum=125.):
        self.expected_commits = expected_commits
        self.expected_changes = expected_changes
        self.expected_tasks_per_user = expected_tasks_per_user
        self.bonus_slope = bonus_slope
        self.maximum = maximum

    def piecewiseLinearBonus(self, effort):
        if effort <= 100:
            return effort

        return round(100 + (effort - 100) * self.bonus_slope, 2)

    def normalize(self, contributions):

        contributions = contributions.copy()

        expected_prs = self.expected_tasks_per_user * 2

        contributions[
            "changes"] = contributions["changes"] / self.expected_changes * 100
        contributions[
            "commits"] = contributions["commits"] / self.expected_commits * 100
        contributions[
            "comments"] = contributions["comments"] / expected_prs * 100
        contributions[
            "contributed"] = contributions["contributed"] / expected_prs * 100

        contributions = contributions.fillna(0.0)

        contributions["effort"] = 5 * contributions[
            "contributed"] + 5 * contributions["commits"] + 3 * contributions[
                "changes"] + 2 * contributions["comments"]

        contributions["effort"] = round(contributions["effort"] / 15, 2)
        contributions["effort"] = contributions["effort"].apply(
            lambda x: self.piecewiseLinearBonus(x))

        contributions["effort"] = contributions["effort"].apply(
            lambda x: min(x, self.maximum))

        return contributions
