import unittest, requests, os, sys
from parameterized import parameterized

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken
from get_data import GetData


class LoginTest(unittest.TestCase):
    url = GetData.url
    def setUp(self):
        self.base_url = self.url + "/user/login"
    @parameterized.expand([( "login_success", "", "", "15458524695", "123", "WEB", "15458524695", "1")])
    def test_login(self, name, checkToken, device_id, loginPass,sessionKey, source, userName, validateCode):
        sessionkey_url = self.url + "/createValidateCode"
        accessKey_url = self.url + "/token/accessToken"
        # 获取图形验证码
        requests.request('post', url=sessionkey_url, data={'sessionKey': sessionKey})
        # 获取accessKey
        response = requests.request('post', url=accessKey_url, data={'userName':userName})
        accessKey = response.json()
        print(accessKey)
        print(len(accessKey))
        #loginpass_encrypt = get_loginpass(accessKey,loginPass)
        testdata = {'checkToken':checkToken, 'device_id':device_id, 'loginPass':loginPass,
                    'sessionKey':sessionKey, 'source':source, 'userName':userName, 'validateCode':validateCode}
        r = requests.request('post', url=self.base_url, data=testdata)
        result = r.json()
        print(result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
