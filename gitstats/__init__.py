from .GithubConnection import GithubConnection
from .StatsCollector import StatsCollector
from .GithubAPIRepository import GithubAPIRepository
from .StatsCalculator import StatsCalculator
from .Reporter import Reporter
from .Templater import Templater

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


def report(access_token, group_name, repository, start, end, excluded_users=[]):
    connection = GithubConnection(access_token, repository)
    repository = GithubAPIRepository(connection.get_repository())
    collector = StatsCollector(repository,
                               start=start,
                               end=end,
                               excluded_users=excluded_users)
    calculator = StatsCalculator(collector)

    templater = Templater()

    reporter = Reporter(group_name, templater.get_template(), calculator)

    return reporter.report()
