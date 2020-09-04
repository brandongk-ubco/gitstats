from .GithubConnection import GithubConnection
from .StatsCollector import StatsCollector
from .PullRequestRepository import PullRequestRepository
from .StatsCalculator import StatsCalculator


def individual_stats(access_token, repository, start, end):
    connection = GithubConnection(access_token, repository)
    repository = PullRequestRepository(connection.get_repository())
    collector = StatsCollector(repository, start=start, end=end)
    calculator = StatsCalculator(collector)
    contributions = calculator.getContributionsByUserAndPR()
    return calculator.getEffortByUserFromContributions(contributions)
