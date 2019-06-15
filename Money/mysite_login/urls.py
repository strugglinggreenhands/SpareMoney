"""mysite_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# mysite_login/urls.py

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from login import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls')),
    url(r'^transaction/', views.transaction),
    url(r'^membership/', views.membership),
    url(r'^modify_info/', views.modify_info),
    url(r'^up_trans/', views.up_trans),
    url(r'^find_trans/', views.find_trans),
    url(r'^my_transaction/', views.my_transaction),
    url(r'^msg_center/', views.msg_center),
    url(r'^accept_trans/', views.accept_trans),
    url(r'^my_doing/', views.my_doing),
    url(r'^my_finish/', views.my_finish),
    url(r'^my_upload/', views.my_upload),
    url(r'^delete_trans/', views.delete_trans),
]
