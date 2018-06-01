import unittest
import requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(dir)
sys.path.append(dir + "/my_function/")
from get_token import get_stampToken, get_chekToken_old, get_chekToken

class ProjectList(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://192.168.3.106:50300/project/list0"

    # @parameterized.expand([#('web_projectCategory_qi', 'WEB', '4', '1', '2', '', '', '','企易融','企易融'),
    #                        # ('web_projectCategory_che', 'WEB', '1', '1', '2', '', '', '','车易融','车易融'),
    #                        # ('web_projectCategory_xin', 'WEB', '2', '1', '2', '', '', '','信易融','信易融'),
    #                        # ('web_projectCategory_fang', 'WEB', '3', '1', '2', '', '', '','房易融','房易融'),
    #                        # ('web_projectCategory_all', 'WEB', '', '1', '5', '', '', '', '车易融','信易融'),
    #                        ('web_page', 'WEB', '', '1', '2', '', '', '', '车易融', '信易融'),
    #                        ('web_page', 'WEB', '', '2', '2', '', '', '', '信易融', '信易融'),
    #                        ])
    #
    # def test_projectls(self, name, source, projectCategory, page, pageSize,
    #                   projectStatus, searchTime, projectNewType, message1,message2):
    #     stampToken = str(get_stampToken())
    #     test_data1 = {'stampToken': stampToken,'source': source,
    #                  'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
    #                  'projectNewType': projectNewType, 'projectCategory': projectCategory}
    #     checkToken = get_chekToken(**test_data1)
    #     test_data = {'stampToken': stampToken, 'checkToken':checkToken, 'source': source,
    #                  'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
    #                  'projectNewType': projectNewType, 'projectCategory': projectCategory,
    #                  'projectStatus':projectStatus}
    #
    #     r = requests.request('get', url=self.base_url, params=test_data)
    #     result = r.json()
    #     print(result)
    #     self.assertEqual(result['code'], 1)
    #     self.assertEqual(result['item']['list'][0]['projectCategory'], message1)
    #     self.assertEqual(result['item']['list'][-1]['projectCategory'], message2)

    @parameterized.expand([('web_inprocess', 'WEB', '', '1', '6', '1', '', '','inProcess','status'),
                           # ('web_finish', 'WEB', '', '1', '6', '2', '', '', 'finish'),
                           # ('web_clear', 'WEB', '', '1', '6', '3', '', '', 'clear'),
                           ])
    def test_projectls_status(self, name, source, projectCategory, page, pageSize,
                              projectStatus, searchTime, projectNewType,message1,message2):
        stampToken = str(get_stampToken())
        test_data1 = {'stampToken': stampToken, 'source': source,
                         'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
                         'projectNewType': projectNewType, 'projectCategory': projectCategory, 'projectStatus':projectStatus}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'checkToken':checkToken, 'source': source,
                     'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
                     'projectNewType': projectNewType, 'projectCategory': projectCategory,
                     'projectStatus':projectStatus}

        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['item']['list'][0][message2], message1)
        self.assertEqual(result['item']['list'][-1][message2], message1)
if __name__ == '__main__':
    unittest.main()
