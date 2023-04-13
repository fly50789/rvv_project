import pytest
import sys,os
from ruamel import yaml
from urllib.parse import urlparse

from datetime import datetime
from time import sleep
from tmp_project.basic import g

'''
scope="session"
scope="package"
scope="module"
scope="class"
scope="function"
'''

def pytest_addoption(parser):
    """
        This function is used to extract input1 and input2 values from the command line
    """
    # parser.addoption('--mock_starter', action='store_true', dest="mock_starter", help='mock the starter')
    # parser.addoption('--local_starter', action='store_true', dest="mock_starter", help='mock the starter')
    # parser.addoption('--show', action='store_true', dest="mock_starter", help='print msg')




@pytest.fixture(scope="session")
def env():
    yield  yaml.safe_load(open('src/tmp_project/config.yml', 'r'))['env']

@pytest.fixture(scope="session")
def env_setting(env):
    g.env = env['LOCAL']
    yield

@pytest.fixture()
def app(env_setting,scope="session"):
    from tmp_project.web_gui import create_app
    yield create_app()



@pytest.fixture()
def test_client(app):
    return app.test_client()
