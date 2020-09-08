class Reporter:

    def __init__(self, group_name, template, calculator):
        self.calculator = calculator
        self.template = template
        self.group_name = group_name

    def report(self):
        users = self.calculator.getUsers()
        contributions = self.calculator.getContributionsByUserAndPR()
        effort = self.calculator.getEffortByUserFromContributions(contributions)
        issues, excluded_issues = self.calculator.getIssues()
        team_score = self.calculator.getTeamScore(users, issues)
        return self.template.render(group_name=self.group_name,
                                    start=self.calculator.get_start(),
                                    end=self.calculator.get_end(),
                                    contributions=contributions,
                                    effort=effort,
                                    issues=issues,
                                    excluded_issues=excluded_issues,
                                    team_score=team_score)
