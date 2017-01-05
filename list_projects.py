import sys
from ReximConfig import get_config
from GithubUrlParser import parse_repo_url
from github import Github

if __name__ == '__main__':
    url = sys.argv[1]
    config = get_config()
    token = config.get("GitHub", "token")
    
    (owner, repo) = parse_repo_url(url)
    g = Github(token)
    for project in  g.get_projects(owner, repo):
        print "%s: %s" % (project["id"], project["name"])
        for column in g.get_columns(project["id"]):
            print "    %s: %s" % (column["id"], column["name"])

