import unittest, requests, os, sys
from parameterized import parameterized

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_auth_token
from get_data import GetData


class UserPersonDataTest(unittest.TestCase):
    url = GetData.url
    def setUp(self):
        self.base_url = self.url + "/user/info"
    def test_person_data(self):
        auth_token = get_chekToken()
        r = requests.request('get', url=self.base_url,params={"authToken":auth_token})



