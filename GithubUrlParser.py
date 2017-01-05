import re

def parse_repo_url(repo_url):
    p = re.compile("https://github.com/(.+)/(.+)")
    m = p.match(repo_url)
    return (m.group(1), m.group(2))

def parse_comment_url(comment_url):
    p = re.compile(r'https://github.com/(.+)/(.+)/issues/\d+#issuecomment-(\d+)')
    m = p.match(comment_url)
    return (m.group(1), m.group(2), m.group(3))

