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
    @parameterized.expand([('name',username)])
    def test_person_data(self, username, password, borrowPermission,openAcctId):
        auth_token = get_auth_token("c2446993", "15458524695")
        r = requests.request('get', url=self.base_url,params={"authToken":auth_token})
        data={'borrowPermission':borrowPermission, 'openAcctId':openAcctId}
        print(r.json()['data'])
        print(type(r.json()['data']))
        self.assertEqual(data, r.json()['data'])
if __name__ == '__main__':
    unittest.main()




