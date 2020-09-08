class Reporter:

    def __init__(self, group_name, template, calculator):
        self.calculator = calculator
        self.template = template
        self.group_name = group_name

    def report(self):
        contributions = self.calculator.getContributionsByUserAndPR()
        effort = self.calculator.getEffortByUserFromContributions(contributions)
        return self.template.render(group_name=self.group_name,
                                    start=self.calculator.get_start(),
                                    end=self.calculator.get_end(),
                                    contributions=contributions,
                                    effort=effort)
