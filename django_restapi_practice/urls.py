"""django_restapi_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

# # 방법 1
# from django.conf.urls import include
# from rest_framework import routers
# from restful_api.views import UserViewSet as uvs

# 방법 2
from restful_api import views

##########



# # 방법 1 에서만 사용
# router = routers.DefaultRouter()
# router.register('users', uvs)
##########

# 장고 Restful API 는 마지막 / 닫아줘야함

urlpatterns = [
    path('admin/', admin.site.urls),

    # # 방법 1
    # path('api/', include(router.urls)),

    # 방법 2
    path('api/users/', views.user_list),
    path('api/users/<_id>/', views.user_select),

    ##########
]