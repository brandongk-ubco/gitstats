class RelativeEffortNormalizer:

    def normalize(self, contributions):

        contributions = contributions.copy()

        contributions["changes"] = contributions["changes"].apply(
            lambda x: min(x, 5000))

        contributions["changes"] = round(
            1.571439 + (-0.01363552 - 1.557803) /
            (1 + (contributions["changes"] / 266.8213)**1.018625), 4)

        contributions["contributed"] = contributions[
            "contributed"] / contributions["contributed"].max() * 100
        contributions["commits"] = contributions["commits"] / contributions[
            "commits"].max() * 100
        contributions["changes"] = contributions["changes"] / contributions[
            "changes"].max() * 100
        contributions["comments"] = contributions["comments"] / contributions[
            "comments"].max() * 100

        contributions = contributions.fillna(0.0)

        contributions["effort"] = 5 * contributions[
            "contributed"] + 5 * contributions["commits"] + 3 * contributions[
                "changes"] + 2 * contributions["comments"]
        contributions["effort"] = contributions["effort"] / contributions[
            "effort"].max() * 100
        return contributions
