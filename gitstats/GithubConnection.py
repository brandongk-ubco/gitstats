from github import Github

class GithubConnection:
    group_name: str
    repository_name: str
    
    def __init__(self, group_name: str, access_token: str, repository_name: str):
        self.group_name = group_name
        self.repository_name = repository_name
        self.api = Github(access_token)

    def get_repository(self):
        return self.api.get_repo(self.repository_name)