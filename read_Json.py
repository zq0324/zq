#coding=utf-8

import json
import xlwt


def get_req(json):
    req = json["paths"]
    for url in req.keys():
        title = url.split('/')
        # print(title[-1])
        name = req[url]['post']['summary']
        #print(name)
        id = req[url]['post']['operationId']
        # print(id)
        param = req[url]['post']['parameters']
        param_dict = dict(param[0])
        path = param_dict['schema']['$ref']
        param_name = path.split('/')
        p_id = get_param(json, param_name[-1])
        str= 'test'+title[-2].title()+id+'\n'
        if title[-2].title() == 'Gateway':
            w_yml(title[-2], id, url, p_id)
        # w_excel(title[-2], name, id, url, 'POST', p_id) # write excel file

def w_yml(path,id,  url, p_id):
    if path.title() == 'Power':
        filename = 'testPower' + id + '.yml'
        name = 'testPower' + id + '\n'

    elif path.title() == 'Signal':
        filename = 'testSignal' + id + '.yml'
        name = 'testSignal' + id + '\n'
    elif path.title() == 'Gateway':
        filename = 'test' + id + '.yml'
        name = 'test' + id + '\n'
    else:
        filename = 'test' + id + '.yml'
        name = 'test' + id + '\n'

    w_file(name)
    with open(filename, 'w+') as f:
        str = """testInterFace: %s
method: POST
url: %s
data: 
 -
   caseName: Correct id
   param:""" % (id, url)
        for i in p_id:
            if i == 'dataMgrId':
                str += '\n     %s: %s' % (i, 'DATAMGRID')
            elif i == 'powerId':
                str += '\n     %s: %s' % (i, 'POWERID')
            elif i == 'screenId':
                str += '\n     %s: %s' % (i, 'SCREENID')
            elif i == 'signalId':
                str += '\n     %s: %s' % (i, 'SIGNALID')
            elif i == 'gatewayId':
                str += '\n     %s: %s' % (i, 'GATEWAYID')

            else:
                str += '\n     %s: %s' % (i, 0)
        str += "\n   result: 0"
        f.write(str)


def w_file(path):
    with open('caselist.txt', 'a') as f:
        f.write(path)


def get_param(json, name):
    req = json['definitions'][name]['properties']
    # print(req.keys())
    # print(req['title'])
    # res = req['properties']
    cc = []
    for q in req.keys():
        cc.append(q)
    return cc


def w_excel(path, name, id, url, method, param=[], msg='msg'):
    n = 0
    wbk = xlwt.Workbook()
    sheet1 = wbk.add_sheet(id)
    sheet1.write(0, 0, "Case_Name")
    sheet1.write(1, 0, name)
    sheet1.write(0, 1, 'Method')
    sheet1.write(1, 1, method)
    sheet1.write(0, 2, 'URL')
    sheet1.write(1, 2, url)
    for n in range(len(param)):
        sheet1.write(0, 3+n, param[n])
    sheet1.write(0, 4 + n, msg)
    path = path.title() + '.' + id + '.xls'
    wbk.save(path)



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