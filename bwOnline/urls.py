# MxOnline/urls.py

import xadmin

from django.urls import path,include,re_path

from django.views.generic import TemplateView
from users.views import *

from organization.views import *

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('captcha/',include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    # 重置密码激活邮箱的url
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    # 机构首页
    path('org_list/',OrgView.as_view(),name = 'org_list'),
]