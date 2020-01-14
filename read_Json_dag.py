#coding=utf-8

import json


def get_req(json):
    req = json["paths"]
    for url in req.keys():
        title = url.split('/')
        devicetype= title[-2]
        if_name = title[-2]+"."+title[-1]
        # print(title[-1])
        # name = req[url]['post']['summary']
        #print(name)
        id = req[url]['post']['operationId']
        # print(id)
        param = req[url]['post']['parameters']
        param_dict = dict(param[0])
        path = param_dict['schema']['$ref']
        param_name = path.split('/')
        p_id = get_param(json, param_name[-1])
        str= 'test'+title[-2].title()+id+'\n'
        # if title[-2].title() == 'Gateway':
        #     w_yml(title[-2], id, url, p_id)
        # w_excel(title[-2], name, id, url, 'POST', p_id) # write excel file
        if len(p_id)>0:
            print "=========="
            w_yml(if_name,devicetype,url,p_id)

def w_yml(if_name, devicetype, url, p_id):
    filename = "dspapi.yml"

    with open(filename, 'a') as f:
        str = """\n%s:
  path: %s
  data:""" % (if_name,url)
        for i in p_id:
            
            if i=="hardwareId":
                if devicetype == 'dataManager':
                    str += '\n    %s: %s' % (i, '$dataMgrId')
                elif devicetype == 'power':
                    str += '\n    %s: %s' % (i, '$powerId')
                elif devicetype == 'signal':
                    str += '\n    %s: %s' % (i, '$signalId')
                elif devicetype == 'screen':
                    str += '\n    %s: %s' % (i, '$screenId')
                elif devicetype == 'gateway':
                    str += '\n    %s: %s' % (i, '$gatewayId')
                elif devicetype == 'camera':
                    str += '\n    %s: %s' % (i, '$cameraId')  
                elif devicetype == 'device':
                    str += '\n    %s: %s' % (i, '$deviceId')   
            elif i == 'bindDevId':
                str += '\n    %s: null' % (i)
            else:
                str += '\n    %s: %s' % (i, 0)
        str += "\n  validate:\n    check_code: 0\n"
        f.write(str)


def w_file(path):
    with open('caselist.txt', 'a') as f:
        f.write(path)


def get_param(json, name):
    req = {}
    try:
        req = json['definitions'][name]['properties']
    except KeyError:
        print name
        return []

    # print(req.keys())
    # print(req['title'])
    # res = req['properties']
    cc = []
    for q in req.keys():
        cc.append(q)
    return cc




#w_yml('datamgrgetid','/api/getid',['dataMgrId'])


with open("api.swagger.json", 'rb') as f:
    rjson = json.load(f)

get_req(rjson)

a = rjson["definitions"]
req = []
rsp = []
rspdata = []

'''
for g in a.keys():
    #print(g)
    if 'Req' in g:
        #print(a[g]['properties'].keys())
        for k in a[g]['properties'].keys():
            req.append(k)
    if 'Rsp' in g:
        print("Response: %s" % a[g]['properties'].keys())
    if 'RspData' in g:
        print("ResponseData: %s" % a[g]['properties'].keys())


print("*"*40)
print(req)
#print(len(gg))
'''