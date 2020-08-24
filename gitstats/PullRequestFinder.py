from . import GithubConnection
import pandas as pd

class PullRequestFinder:

    def __init__(self, connection: GithubConnection):
        self.connection = connection

    def find(self, start, end):
        return pd.DataFrame()
