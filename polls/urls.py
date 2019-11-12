from django.conf.urls import url

from . import views
'''
将根urlconf指向该polls.urls模块
添加的导入django.urls.include
并将插入 include()到urlpatterns列表中
该include()功能允许引用其他URLconf。

每当Django遇到时include()，它都会截断直到该时间点匹配的
URL的任何部分，并将剩余的字符串发送到包含的URLconf中
以进行进一步处理。

背后的想法include()是简化URL的即插即用。

该path()函数传递了四个参数，两个是必需的 route和view，
以及两个可选的kwargs和name。

path()参数：route
route是包含URL模式的字符串。在处理请求时，Django从第一个模式开始，urlpatterns然后沿列表向下移动，将请求的URL与每个模式进行比较，直到找到匹配的URL。

模式不搜索GET和POST参数或域名。例如，在对的请求中https://www.example.com/myapp/，URLconf将寻找 myapp/。在请求中https://www.example.com/myapp/?page=3，URLconf也将寻找myapp/。

path()参数：view
当Django找到匹配的模式时，它将使用HttpRequest对象作为第一个参数，并将路线中所有“捕获的”值作为关键字参数，调用指定的view函数。我们将举一个例子。

path()参数：kwargs
可以在字典中将任意关键字参数传递给目标视图。在本教程中，我们将不使用Django的此功能。

path()参数：name
命名URL可以使您在Django中的其他地方（尤其是在模板内部）明确地引用它。这项强大的功能可让您仅触摸单个文件即可对项目的URL模式进行全局更改。

'''
urlpatterns=[
    # views.index不能带括号！
    # url('',views.current_datetime,name='index'),
    # url('^polls$',views.index,name='index'),
]

