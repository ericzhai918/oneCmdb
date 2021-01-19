# -*- coding:utf-8 -*-
__author__ = 'Leon.Zhai'
__date__ = '2021/1/7 14:03'

from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework.documentation import include_docs_urls

from publicinfo.views import firms, firm_detail
from publicinfo.views import Firms, Firms_detail
from publicinfo.views import Firms3, Firms_detail3
from publicinfo.views import Firms4, Firms_detail4
from publicinfo.views import Firms5
from publicinfo.views import Firms6

Firms5_View_list = Firms5.as_view({'get': 'list', 'post': 'create'})
Firms_detail5 = Firms5.as_view({"get": "retrieve",
                                "put": "update",
                                "delete": "destroy"})

'''
            list,create,retrieve,update,destroy对应的是
            
            mixins.ListModelMixin,l
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.CreateModelMixin,
            mixins.DestroyModelMixin
'''

router = DefaultRouter()
router.register('firms6', Firms6, basename='firms')

urlpatterns = [
    path('firms/', firms),
    re_path('firms/(\d+)/', firm_detail),

    path('firms2/', Firms.as_view()),
    re_path('firms2/(\d+)/', Firms_detail.as_view()),

    path('firms3/', Firms3.as_view()),
    re_path('firms3/(?P<pk>[0-9]+)/', Firms_detail3.as_view()),
    # 需要加变量pk，混合模式必须这么写

    path('firms4/', Firms4.as_view()),
    re_path('firms4/(?P<pk>[0-9]+)/', Firms_detail4.as_view()),

    path('firms5/', Firms5_View_list),
    re_path('firms5/(?P<pk>[0-9]+)/', Firms_detail5),

    path('', include(router.urls)),
    path('docs/', include_docs_urls('cmdb接口文档'))
]
