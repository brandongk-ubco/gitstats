class RelativeEffortNormalizer:

    def normalize(self, contributions):

        contributions = contributions.copy()

        contributions["changes"] = contributions["changes"].apply(
            lambda x: min(x, 5000))
        contributions["changes"] = round(
            1.571439 + (-0.01363552 - 1.557803) /
            (1 + (contributions["changes"] / 266.8213)**1.018625), 4)

        contributions["commits"] = contributions["commits"].apply(
            lambda x: min(x, 50))
        contributions["commits"] = round(
            1648.3478 + (0.00219986 - 1648.35) /
            (1 + (contributions["changes"] / 1972891000)**0.4007762), 4)

        contributions["comments"] = contributions["comments"].apply(
            lambda x: min(x, 100))
        contributions["comments"] = round(
            796.8409 + (0.01079994 - 796.8517) /
            (1 + (contributions["comments"] / 4347145000)**0.3597313), 4)

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
        contributions["effort"] = contributions["effort"].fillna(0)
        contributions["effort"] = contributions["effort"].apply(
            lambda x: x if x <= 50 else round(106.0259 + (
                -86433570 - 106.0259) / (1 + (x / 0.5517194)**3.162139)))
        return contributions
