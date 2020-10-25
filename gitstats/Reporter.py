class Reporter:

    def __init__(self, group_name, template, calculator, normalizer):
        self.calculator = calculator
        self.template = template
        self.group_name = group_name
        self.normalizer = normalizer

    def report(self):
        users = self.calculator.getUsers()
        contributionsByUserAndPR = self.calculator.getContributionsByUserAndPR()
        contributionsByUser = self.calculator.getContributionsByUser(
            contributionsByUserAndPR)

        effort = self.normalizer.normalize(contributionsByUser)
        issues, excluded_issues = self.calculator.getIssues()
        team_score = self.calculator.getTeamScore(users, issues)
        final_scores = self.calculator.getFinalScores(effort, team_score)
        return self.template.render(
            group_name=self.group_name,
            start=self.calculator.get_start(),
            end=self.calculator.get_end(),
            contributionsByUserAndPR=contributionsByUserAndPR,
            contributionsByUser=contributionsByUser,
            effort=effort,
            issues=issues,
            excluded_issues=excluded_issues,
            team_score=team_score,
            final_scores=final_scores)
