import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_chekToken, get_auth_token, get_stampToken


class MessageTest(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/msg/msg"

    def test_aPPmessage(self):
        stampToken = str(get_stampToken())
        authToken = get_auth_token(userName='15558524695', loginPass='123456')
        test_data1 = {'stampToken': stampToken, 'authToken': authToken, 'messageFlag': '', 'page': '', 'isRead': '',
                      'source': 'APP'}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'authToken': authToken, checkToken: 'checkToken',
                     'messageFlag': '', 'page': '', 'isRead': '', 'source': 'APP'}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)

if __name__ == '__main__':
    unittest.main()

