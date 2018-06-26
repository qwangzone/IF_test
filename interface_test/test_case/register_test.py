import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_chekToken, get_auth_token, get_stampToken, get_loginpass


class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.url = GetData.url
        self.base_url = self.url + "/user/register"

    def SMS_resistercode(self, sessionKey="123", mobilephone="12345678910", smsType="Register"):
        #获取图形验证码
        sessionkey_url = self.url + "/createValidateCode"
        requests.request('post', url=sessionkey_url, data={'sessionKey': sessionKey})
        #获取手机验证码
        url= self.url + "/sendMobileCode"
        test_data = {'validateCode': '1', 'sessionKey': sessionKey, 'mobile': mobilephone, 'smsType': smsType,
                     'userId': ''}
        r = requests.request('post', url=url, data=test_data)
        result = r.json()
        print(result)
        mobileCode = result['data']
        return mobileCode

    @parameterized.expand([("test_register_success", "12345678910", "123456", "Register", "appstore", "APP")])
    def test_register(self, name, mobile, password, smsType, channel, source):
        accessKey_url = self.url + "/token/accessToken"
        response = requests.request('post', url=accessKey_url, data={'userName': mobile})
        access_key = response.json()['data']
        loginpass_encrypt = get_loginpass(access_key, password)
        mobileCode = str(SMS_resistercode(mobilephone=mobile, smsType=smsType))
        test_data1 = {'mobile': '12345678910', 'mobileCode': mobileCode, 'loginPass': loginpass_encrypt,
                      'channel': channel, 'recommendCode': '', 'adid': '', 'source': source}
        checkToken = get_chekToken(**test_data1)
        test_data = {'mobile': '12345678910', 'mobileCode': mobileCode, 'loginPass': loginpass_encrypt,
                     'channel': channel, 'recommendCode': '', 'adid': '', 'checkToken': checkToken, 'source': source}
        r = requests.request('post', url=self.base_url, data=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['data']['mobile'], mobile)


if __name__ == '__main__':
    unittest.main()




