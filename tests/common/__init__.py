import os


def is_executing_under_continuous_integration_server():
    return os.getenv('CI', 'false') == 'true'


def set_support_environment(path):
    os.environ['SUPPORT_PATH'] = '%s%s' % (path, '/support/')


def get_support_path():
    return os.getenv('SUPPORT_PATH', '%s%s' % (os.path.dirname(__file__), '/support/'))