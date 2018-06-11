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
    @parameterized.expand([('test_OpenSumaPay_success1', 'c2446993', '15458524695')])
    def test_OpenSumaPay_success(self, name, username, password):
        """开户成功并设置交易密码成功"""
        auth_token = get_auth_token(username, password)
        r = requests.request('get', url=self.base_url, params={"authToken": auth_token})
        #data={'borrowPermission': borrowPermission, 'openAcctId':openAcctId}
        result = r.json()
        print(result)
        #print(r.json()['data'])
        # print(type(r.json()['data']))
        # self.assertEqual(data, r.json()['data'])

if __name__ == '__main__':
    unittest.main()




