import threading,pytest,os,sys,requests
from pprint import pprint

from time import sleep,time
from datetime import datetime,timedelta


#g.user = User_event
from  tmp_project.basic import g

import tmp_project
def test_example():
    print()
    assert True,'example'



def test_version_info_1(test_client):
    print()
    #curl -X GET "https://127.0.0.1:8043/api/v1/version_info/" -H "accept: application/json"
    r = test_client.get('/api/v1/version_info/')
    assert r.status_code,'version info status code\nresp:{}'.format(r.json)
    assert 'scheduler' in r.json,'version info check key `scheduler`\nresp:{}'.format(r.json)

if __name__ ==              "__main__":
    pytest.main(['--disable-pytest-warnings',
                 'tests/test_api.py::test_example',
                #'tests/test_api.py::test_version_info_1',
                ])
