# coding=utf-8
# @FileName: test_list.py
# @Author: ZhengQiang
# Date: 2020/1/3 5:16 下午


def check_headers(headers_list, append):
    result = []
    status = False
    if headers_list is None or headers_list == '' or len(headers_list) == 0:
        return [append]
    else:
        for k in append.keys():
            for h in headers_list:
                if h['name'].lower() == k.lower():
                    break
            else:
                result.append({'name': k, 'value': append[k], 'description': 'auto create'})
        return result+headers_list


bb = [{'name': 'content-type', 'value': 'application/json'}, {'name': 'keytest', 'value': 'ie12313'}]
cc = {'Content-Type3': 'application/json', 'Content-Type2': 'application/json'}
aa = check_headers(bb, cc)
print(aa)
