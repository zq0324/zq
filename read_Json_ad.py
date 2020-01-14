#coding=utf-8

import json


def get_req(json):
    req = json["paths"]
    req_param = json["definitions"]
    baseurl = json["basePath"]
    for url in req.keys():
        if_module = url.split("/")[1]
        for method, item in req[url].items():
            if_summary = item["summary"]
            if_name = item["operationId"].split("Using")[0]
            if_name = if_module+"."+if_name
            parameters = {}
            params = {}

            data = {}
            if "parameters" in item.keys():
                parameters = item["parameters"]
                if method == "get" or method == "delete":
                    for p in parameters:
                        if "schema" in p.keys():
                            tmp1 = "optional"
                            if p["required"]=="true":
                                tmp1 = "required"

                            tmp = p["in"] +"  # "+tmp1+" "+p["description"]
                            params[p["name"]] = tmp
                        else:
                            tmp1 = "optional"
                            if p["required"]=="true":
                                tmp1 = "required"

                            tmp = p["type"] +"  # "+tmp1+ " "+p["description"]
                            params[p["name"]] = tmp
                else:
                    p = parameters[0]
                    if p["in"] == "formData":
                        data[p["name"]]=p["type"]+ "  # " +p["description"]
                    elif "schema" in p.keys():
                        tmp = p['schema']['$ref'].split("/")[-1]
                        if tmp in req_param.keys():
                            paramtmp = req_param[tmp]["properties"]
                            for key, value in paramtmp.items():
                                str_tmp = ""
                                if "type" in value.keys():
                                    str_tmp = value["type"] + "  # "
                                if "description" in value.keys():
                                    str_tmp += value["description"]

                                data[key] = str_tmp
                        else:
                            data["error"] = "not find"

            w_yml(if_name, if_summary, method, baseurl+url, data, params)



def w_yml(if_name, if_summary,method, url, data,params):
    filename = "boss_api.yml"
    with open(filename, 'a') as f:
        str1 = """\n%s:
  summary: %s
  method: %s
  path: %s\n""" % (if_name,if_summary,method,url)
        if len(data) > 0:
            str1 += "  json: \n"
            for key,value in data.items():
                str1 += "    %s: # %s  \n" % (key, value)
        elif len(params) > 0:
            str1 += "  params: \n"
            for key,value in params.items():
                str1 += "    %s: # %s  \n" % (key, value)
        # str1 += "  validate: \n" \
        #         "    check_code: 0\n"
        f.write(str1)


def w_file(path):
    with open('caselist.txt', 'a') as f:
        f.write(path)


def get_param(json, name):
    req = {}
    try:
        req = json['definitions'][name]['properties']
    except KeyError:
        print(name)
        return []

    # print(req.keys())
    # print(req['title'])
    # res = req['properties']
    cc = []
    for q in req.keys():
        cc.append(q)
    return cc




#w_yml('datamgrgetid','/api/getid',['dataMgrId'])


with open("ad_api.json", 'rb') as f:
    rjson = json.load(f)


get_req(rjson)





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