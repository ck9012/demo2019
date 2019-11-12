
from django.http import HttpResponse,Http404
import datetime


from django.shortcuts import render_to_response
from django.template import Context,Template
from django.template.loader import get_template

'''
第一个视图   polls
要调用该视图，需要将其映射到url，需要一个urlconf，
在同级创建一个urls.py文件
'''
def index(request):
    return HttpResponse('hello,world. you are at the polls index .')

def current_datetime(request):


    # now=datetime.datetime.now()
    # html='<html><body><h3>it is now %s.</h3></body></html>'% now   #写法1
    # return HttpResponse(html)

    # now=datetime.datetime.now()
    # t=Template('<html><body><h2>it is now {{current_date}}.</h2></body></html>')    #写法2
    # html=t.render(Context({'current_date':now}))
    # return HttpResponse(html)

    # now=datetime.datetime.now()
    # 直接用项目内的路径就可以
    # f=open('templates\latest_books.html')   #写法3
    # t=Template(f.read())
    # f.close()
    # # 输出时间，但不是每秒刷新
    # # html=t.render(Context({'current_datetime':now.isoformat()[:-7],'name':'abc'}))
    # html=t.render(Context({'current_datetime':now.isoformat()[:-7]}))
    # return HttpResponse(html)



    # now=datetime.datetime.now()
    # t = get_template('latest_books.html')   #写法4
    # # 网上的例子和实际不一样
    # html = t.render({'current_datetime': now,'name':'tom'})
    # return HttpResponse(html)



    # now=datetime.datetime.now()
    # return render_to_response('latest_books.html',{'current_datetime': now.isoformat()[:-7],'name':'alin'})  #写法5


    # name='alin'   #写法6
    # current_datetime=datetime.datetime.now().isoformat()[:-7]
    # #使用 locals() 时要注意是它将包括 所有 的局部变量，它们可能比你想让模板访问的要多。 在前例中， locals() 还包含了 request 。
    # return render_to_response('latest_books.html',locals())

    # 加子目录

    current_datetime=datetime.datetime.now().isoformat()[:-7]
    return render_to_response('tarticle/tarticle.html',locals())