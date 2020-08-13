from dataclasses import dataclass
from github import Github

@dataclass
class GithubConnection:
    group_name: str
    access_token: str
    repository_name: str
    branch_name: str = "master"
    
    def __init__(self, group_name: str, access_token: str, repository_name: str, branch_name: str = "master"):
        self.group_name = group_name
        self.repository_name = repository_name

        self.api = Github(access_token)
        self.repository = self.api.get_repo(self.repository_name)
        self.branch = self.repository.get_branch(self.branch_name)
