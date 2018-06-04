import unittest
import os, sys
import requests
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_token import get_stampToken, get_chekToken_old, get_chekToken
from get_data import GetData

class ProjectcreditAssignList(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/project/creditAssignList"

    def test1_biaodi(self):
        stampToken = str(get_stampToken())
        test_data1 = {'stampToken': stampToken, 'page': '1', 'pageSize': '10', 'source': 'WEB', 'nextPlanPay': '',
                     'searchTime': '4', 'interestRate': ''}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'checkToken': checkToken, 'page': '1', 'pageSize': '10', 'source': 'WEB',
                     'nextPlanPay': '', 'searchTime': '4', 'interestRate': ''}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)

if __name__ == "__main__":
    unittest.main()


