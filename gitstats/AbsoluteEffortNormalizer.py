class AbsoluteEffortNormalizer:

    def __init__(self, expected_changes, expected_commits,
                 expected_tasks_per_user):
        self.expected_commits = expected_commits
        self.expected_changes = expected_changes
        self.expected_tasks_per_user = expected_tasks_per_user

    def normalize(self, contributions):

        contributions = contributions.copy()

        expected_prs = self.expected_tasks_per_user * 2

        contributions["changes"] = contributions["changes"].apply(
            lambda x: min(x, self.expected_changes))
        contributions["commits"] = contributions["commits"].apply(
            lambda x: min(x, self.expected_commits))
        contributions["comments"] = contributions["comments"].apply(
            lambda x: min(x, expected_prs))
        contributions["contributed"] = contributions["contributed"].apply(
            lambda x: min(x, expected_prs))

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

        return contributions
