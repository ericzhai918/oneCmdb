# -*- coding:utf-8 -*-
__author__ = 'Leon.Zhai'
__date__ = '2021/1/7 13:33'

from rest_framework import serializers
from publicinfo.models import FirmList


class FirmListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    firm_name = serializers.CharField(required=True, max_length=128,help_text='厂商名称')
    firm_owner = serializers.CharField(required=True, max_length=128,help_text='厂商联系人')
    firm_phone = serializers.IntegerField(required=True,help_text='厂商联系电话')

    def create(self, validated_data):
        return FirmList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firm_name = validated_data.get('firm_name', instance.firm_name)
        instance.firm_owner = validated_data.get('firm_owner', instance.firm_owner)
        instance.firm_phone = validated_data.get('firm_phone', instance.firm_phone)
        instance.save()
        return instance

    # def to_representation(self, instance):
    #     represent_data = super().to_representation(instance)
    #     represent_data['firm_phone']={
    #         'firm_phone':instance.firm_phone,
    #         'paln-b':'021-88888888'
    #     }
    #     represent_data['test']='翻版必究'
    #     return represent_data
    #
    # def to_internal_value(self, data):
    #     #反序列化第一步，拿到的是前端提交过来的原始QueryDict
    #     #如有些字段不需要用户传入，自己这里处理，添加字段
    #     return super().to_internal_value(data)


