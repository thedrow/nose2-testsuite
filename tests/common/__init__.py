import os


def is_executing_under_continuous_integration_server():
    return os.getenv('CI', 'false') == 'true'