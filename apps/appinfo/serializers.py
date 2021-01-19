# -*- coding:utf-8 -*-
__author__ = 'Leon.Zhai'
__date__ = '2021/1/7 11:05'

from rest_framework import serializers
from appinfo.models import SystemList, SubSystemList


class SystemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemList
        fields = "__all__"


class SubSystemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSystemList
        fields = "__all__"
