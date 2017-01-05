import requests
import re

GITHUB_API_BASE_URL="https://api.github.com"
PREVIEW_HEADER = { "Accept": "application/vnd.github.inertia-preview+json" }

class Github:
    def __init__(self, token):
        self._token = token
 
    def get_comment_text(self, owner, repo, comment_id):
        t = "%s/repos/%s/%s/issues/comments/%s?access_token=%s"
        url = t % (GITHUB_API_BASE_URL, owner, repo, comment_id, self._token)
        return requests.get(url).json()["body"]

    def create_note_card(self, column_id, text):
        t = "%s/projects/columns/%s/cards?access_token=%s"
        url = t % (GITHUB_API_BASE_URL, column_id, self._token)
        return requests.post(url,
                             json = { "note": text },
                             headers = PREVIEW_HEADER).json()

    def get_projects(self, owner, repo):
        t = "%s/repos/%s/%s/projects?access_token=%s"
        url = t % (GITHUB_API_BASE_URL, owner, repo, self._token)
        return requests.get(url, headers = PREVIEW_HEADER).json()

    def get_columns(self, project_id):
        t = "%s/projects/%s/columns?access_token=%s"
        url = t % (GITHUB_API_BASE_URL, project_id, self._token)
        return requests.get(url, headers = PREVIEW_HEADER).json()
