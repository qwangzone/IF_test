from datetime import datetime
import hashlib
def get_stampToken():
    return int(datetime.now().timestamp()*1000)

def get_chekToken_old(*args):
    md5 = hashlib.md5()
    str_code = ""
    for i in args:
        str_code = str_code + i
   # a = list(args)
    #a.sort()
    md5.update(str_code.encode('utf-8'))
    return md5.hexdigest()

def get_chekToken(**kwargs):
    md5 = hashlib.md5()
    str_code = ""
    values = list(dict(sorted(kwargs.items(),key=lambda d :d[0])).values())
    for i in values:
        str_code = str_code + i
    md5.update((str_code+"689d3783957d65d57229ba3dc70a20fb").encode('utf-8'))
    return md5.hexdigest()

# #print(get_chekToken("wq","sa"))
#
# a = {"b":"12", "a":"89","hj":"67"}
# def sortedDictValues1(adict):
#     keys = list(adict.keys())
#     keys.sort()
#     return [adict[key]  for key  in keys]
# #print(sortedDictValues1(a))
#
# b = sorted(a.items(),key=lambda d :d[1])
# print(a.items())
# print(dict(b).values())