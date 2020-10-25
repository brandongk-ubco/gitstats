from .GithubConnection import GithubConnection
from .StatsCollector import StatsCollector
from .GithubAPIRepository import GithubAPIRepository
from .StatsCalculator import StatsCalculator
from .Reporter import Reporter
from .Templater import Templater
from .TimeConverter import TimeConverter
from .RelativeEffortNormalizer import RelativeEffortNormalizer
from github import Github

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


def check_for_updates():
    if __version__ == "alpha":
        return
    g = Github()
    gitstats_repo = g.get_repo("brandongk-ubco/gitstats")
    latest_tag = gitstats_repo.get_latest_release().tag_name
    assert __version__ == latest_tag[
        1:], "Newer version of gitstats %s found.  Please upgrade." % latest_tag


def report(access_token, group_name, repository, start, end, excluded_users=[]):
    check_for_updates()
    start = TimeConverter.utc_to_pacific(start)
    end = TimeConverter.utc_to_pacific(end)
    connection = GithubConnection(access_token, repository)
    repository = GithubAPIRepository(connection.get_repository())
    normalizer = RelativeEffortNormalizer()
    collector = StatsCollector(repository,
                               start=start,
                               end=end,
                               excluded_users=excluded_users)
    calculator = StatsCalculator(collector)

    templater = Templater()

    reporter = Reporter(group_name, templater.get_template(), calculator,
                        normalizer)

    return reporter.report()
