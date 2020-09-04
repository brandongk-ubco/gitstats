from github import Github


class GithubConnection:
    repository_name: str

    def __init__(self, access_token: str, repository_name: str):
        self.repository_name = repository_name
        self.api = Github(access_token)

    def get_repository(self):
        return self.api.get_repo(self.repository_name)
