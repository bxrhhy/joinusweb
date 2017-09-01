from django.conf.urls import url
from . import views
urlpatterns=[
    url('^tips/',views.tips,name='tips'),
    url('^tips_done/',views.tips_done,name='tips_done'),
    url('^home/',views.home,name='home'),
    url('^new/', views.new, name='new'),
    url('^add/action', views.add_action, name='add_action'),
    url('^del/action', views.del_action, name='del_action'),
    url('^d_action', views.del_action1, name='del_action1'),
    url('^done_action', views.done_action, name='done_action1'),

]