from django.urls import path,re_path
from . import views

app_name = 'userauth'
urlpatterns = [
    path('zhuce/',views.zhuce,name='zhuce'),
    path('login/',views.login,name='login'),
    path('adduser/',views.adduser,name='adduser'),
    path('index1/',views.index1,name='index1'),
    # re_path('^article/.*', views.article,name='article'),
    path('<int:con_id>/details/', views.details,name='details'),
]