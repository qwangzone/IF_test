import configparser, os
class GetData:
    dir = os.path.dirname(os.path.abspath(__file__))
    file_path = dir + "/url_data.ini"
    cf = configparser.ConfigParser()
    cf.read(file_path, encoding='utf-8')
    url = cf.get("url", "test_url")
