import json

data={
    'abd':1,
    'login':'zhangsan',
    'password':'abcde',
}

json_str=json.dumps(data)
# print('字典:',data)
# print('原始数据：',repr(data))
# print('json对象：',json_str)

data2=json.loads(json_str)
print(data2)
print('name:',data2['login'])
print('abd:',data2['abd'])