# coding=utf-8
import requests
import jsonpath

# url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
#
# response = requests.get(url,headers=header)
# data = response.json()

jj = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
            {"category": "fiction",
             "author": "Herman Melville",
             "title": "Moby Dick",
             "isbn": "0-553-21311-3",
             "price": 8.99
             },
            {"category": "fiction",
             "author": "J. R. R. Tolkien",
             "title": "The Lord of the Rings",
             "isbn": "0-395-19395-8",
             "price": 22.99
             }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}
# tmp = jsonpath.jsonpath(jj, "$..book[(@.length-1)]", debug=1)

da = {
    "code": 0,
    "message": "OK",
    "data": [{
        "accessToken": "ad50943a38916d2b9b7a5a0a6989a251bb42c28b822ab31372127b22cbd38aabca9a91cb5b53a9a8",
        "expiresTime": 1561080593059,
        "data": {
            "res": 123123
        }
    },
        {
            "accessToken": "ad50943a38916d2b9b7a5a0a6989a251bb42c28b822ab31372127b22cbd38aabca9a91cb5b53a9a8",
            "expiresTime": 1561080593059,
            "data": {
                "res": "kill"
            }
    }]
}
res = jsonpath.jsonpath(da,"$.data[0].data.*",debug=1)

print(res)
