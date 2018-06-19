import HTMLTestRunner, unittest, os
dir = os.path.dirname(os.path.abspath(__file__))
sta_dir = dir + "/test_case"
discover = unittest.defaultTestLoader.discover(start_dir=sta_dir, pattern="*_test.py")
filename = dir + "/report/apd_interfaceTest_report.html"
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="阿朋贷接口测试报告",description="阿朋贷接口", verbosity=2)
print(discover.countTestCases())
# runner.run(discover)
# fp.close()