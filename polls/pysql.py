# import pymysql
from django.shortcuts import render_to_response, redirect

from books.models import Publisher

'''
手动连接数据查询资料
'''

# def pysql(request):
#
#     # 写法1
#     db=pymysql.connect(
#         host='localhost',
#         user='root',
#         password='123456',
#         database='portal',
#         charset='utf8'
#     )
#     # 光标 cursor
#     cursor=db.cursor()
#     cursor.execute('select loginname from user limit 0,20')
#     name=cursor.fetchall()
#     db.close()
#     return render_to_response('latest_books.html',{'name':name})

# print('=========================')
# try:
#     conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='polls', port=3306, charset='utf8')
#     cur = conn.cursor()
#     cur.execute('select version()')
#     version = cur.fetchone()
#     print(version)
#     print('ok')
#     cur.close()
#     conn.close()
# except  Exception:
#     print("发生异常")

def pysql(request):
    # all=Publisher.objects.all() #获取所有数据
    # return render_to_response('tarticle/tarticle.html',locals())

    all=Publisher.objects.filter(name__contains='a').order_by('-id')
    # all=Publisher.objects.get(id=1)   #会报错
    return render_to_response('tarticle/tarticle.html',locals())




# 增
def add(request):
    # obj=Publisher()
    # obj.save()
    Publisher.objects.create(name='abc',address='home',city='dal')
    return render_to_response('tarticle/tarticle.html', {'name': 'tom'})


def delete(request):
    Publisher.objects.filter(id=5).delete()
    return render_to_response('tarticle/tarticle.html', {'name': 'tom'})


def update(request):
    # Publisher.objects.get(id=4)._do_update(country='abd')
    Publisher.objects.filter(id=4).update(website='1abd')
    return  render_to_response('tarticle/tarticle.html',{'name':'tom'})


# https://jingyan.baidu.com/article/11c17a2cd708c2f446e39d02.html