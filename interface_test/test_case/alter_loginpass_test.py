import unittest, requests, os, sys
from parameterized import parameterized

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData

class AlterLoginpassTest(unittest.TestCase):
    url = GetData.url
    def setUp(self):
        self.base_url = self.url + "/user/savePassword"

    @parameterized.expand([('success', '15458524695','15458524695','WEB')])
    def test_alter_loginpass(self,name,oldPassword,newPassword,source):
        auth_token = get_auth_token("c2446993", "15458524695")
        data={'authToken':auth_token, 'oldPassword':oldPassword, 'newPassword':newPassword, 'source':source}
        r = requests.request('post', url=self.base_url, data=data)
        print(r.json())

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()