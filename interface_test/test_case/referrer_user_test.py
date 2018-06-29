import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class ReferrerUserTest(unittest.TestCase):
    url = GetData.url

    def setUp(self):
        self.base_url = self.url + "/recommend"

    def test1(self):
        authtoken = get_auth_token()
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'page': '', 'source': 'APP'}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': str(stampToken),'checkToken':chcketoken,
                       'page': '', 'source': 'APP'}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()

    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()
