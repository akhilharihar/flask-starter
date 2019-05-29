from .utils import Path


def index():
    return 'flask app'


url_rules = [
    Path(rule='/', endpoint='index', view_func=index)
]
