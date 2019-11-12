from django import db
import json

from django.db import connection
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
# from portal.models import *
from django.template import RequestContext




def findarticle(request):
    # tarticle=TArticle.objects.filter(column_id=19)
    with connection.cursor() as cursor:
        # 光标.执行
        cursor.execute('select * from t_article LEFT JOIN t_column on t_article.column_id=t_column.id limit 2')
        # 返回二维数组
        tarticle=cursor.fetchall()
        return render_to_response('tarticle/tarticle.html',locals())

def base1(request,one):

    return render_to_response('tarticle/tarticle.html',locals())


def index(request):
    return render_to_response('tarticle/tarticle.html',context_instance=RequestContext(request))


def do_save_info(request):
    result = {'result': 'save success'}
    try:
        data = json.loads(request.body)
        username = data.get("username", None)
        password = data.get("password", None)
        models.do_save_info(username, password)
    except :
        result['result'] = 'save error'
    return HttpResponse(json.dumps(result))



def black_page(request):
    d={'a':323,'b':1098}

    return render_to_response('demo.html',locals())