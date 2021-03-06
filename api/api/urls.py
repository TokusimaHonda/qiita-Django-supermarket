"""api URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from api.settings import MEDIA_ROOT
import xadmin
from goods.views import GoodsListViewSet
from goods.views import CategoryViewSet

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet)
router.register(r'categorys', CategoryViewSet, base_name="categorys")

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('xadmin/', xadmin.site.urls),
    re_path('^', include(router.urls)),
    path('docs/', include_docs_urls(title="shop")),
]
