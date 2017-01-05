import sys

from ConfigParser import ConfigParser
from github import Github
from GithubUrlParser import parse_comment_url
from ReximConfig import get_config

if __name__ == '__main__':
    url = sys.argv[1]
    config = get_config()

    column_id = config.get("Comment2card", "column_id")
    token = config.get("GitHub", "token")

    (owner, repo, comment_id) = parse_comment_url(url)

    g = Github(token)
    print g.create_note_card(column_id,
                             g.get_comment_text(owner, repo, comment_id))
