from ConfigParser import ConfigParser
from os.path import expanduser

def get_config():
    filename = expanduser("~/.rexim-config")
    config = ConfigParser()
    config.read(filename)
    return config
