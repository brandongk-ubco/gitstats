class AbsoluteEffortWithBonusNormalizer:

    def __init__(self,
                 report_weeks,
                 expected_changes_per_week=200,
                 expected_commits_per_week=4,
                 expected_tasks_per_week=2,
                 bonus_slope=0.25,
                 maximum=125.):
        self.expected_commits = expected_commits_per_week * report_weeks
        self.expected_changes = expected_changes_per_week * report_weeks
        # Double the PRs to account for work-on and review work.
        self.expected_prs = expected_tasks_per_week * report_weeks * 2
        self.bonus_slope = bonus_slope
        self.maximum = maximum

    def piecewiseLinearBonus(self, effort):
        if effort <= 100:
            return effort

        return round(100 + (effort - 100) * self.bonus_slope, 2)

    def normalize(self, contributions):

        contributions = contributions.copy()

        contributions[
            "changes"] = contributions["changes"] / self.expected_changes * 100
        contributions[
            "commits"] = contributions["commits"] / self.expected_commits * 100
        contributions[
            "comments"] = contributions["comments"] / self.expected_prs * 100
        contributions["contributed"] = contributions[
            "contributed"] / self.expected_prs * 100

        contributions["changes"] = contributions["changes"].apply(
            lambda x: self.piecewiseLinearBonus(x))
        contributions["changes"] = contributions["changes"].apply(
            lambda x: min(x, self.maximum))

        contributions["commits"] = contributions["commits"].apply(
            lambda x: self.piecewiseLinearBonus(x))
        contributions["commits"] = contributions["commits"].apply(
            lambda x: min(x, self.maximum))

        contributions["comments"] = contributions["comments"].apply(
            lambda x: self.piecewiseLinearBonus(x))
        contributions["comments"] = contributions["comments"].apply(
            lambda x: min(x, self.maximum))

        contributions["contributed"] = contributions["contributed"].apply(
            lambda x: self.piecewiseLinearBonus(x))
        contributions["contributed"] = contributions["contributed"].apply(
            lambda x: min(x, self.maximum))

        contributions = contributions.fillna(0.0)

        contributions["effort"] = 5 * contributions[
            "contributed"] + 5 * contributions["commits"] + 3 * contributions[
                "changes"] + 2 * contributions["comments"]

        contributions["effort"] = round(contributions["effort"] / 15, 2)

        return contributions
