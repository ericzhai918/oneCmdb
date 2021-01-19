from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet

from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from publicinfo.models import FirmList
from publicinfo.serializers import FirmListSerializer


# Create your views here.

# -----------------------------------Django REST framework 函数视图方式使用------------------------------

@api_view(['GET', 'POST'])  # 只允许get post请求
def firms(request, *args, **kwargs):
    # 获取Firm所有的对象，以及新增一个Firm对象

    if request.method == 'GET':
        serializer = FirmListSerializer(FirmList.objects.all(), many=True)  # 将所有的FirmList模型进行序列化
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FirmListSerializer(data=request.data)  # 通过api_view会自动转换request数据为json
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def firm_detail(request, pk, *args, **kwargs):
    # 对单个Firm对象删改查

    try:
        firm = FirmList.objects.get(pk=pk)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FirmListSerializer(firm)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = FirmListSerializer(firm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        firm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------------------Django REST framework 类视图方式使用------------------------------
class Firms(APIView):
    # 获取Firm所有的对象，以及新增一个Firm对象

    def get(self, request, format=None):
        query = FirmList.objects.all()
        serializer = FirmListSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FirmListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Firms_detail(APIView):
    # 对单个Firm对象删改查

    def get_firm(self, pk):
        try:
            return FirmList.objects.get(pk=pk)
        except ModuleNotFoundError:
            return Http404

    def get(self, request, pk, *args, **kwargs):
        firm = self.get_firm(pk)
        serializer = FirmListSerializer(firm)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        firm = self.get_firm(pk)
        serializer = FirmListSerializer(firm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        firm = self.get_firm(pk)
        firm.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# -----------------------------------Django REST framework 混合模式mixins视图使用------------------------------

class Firms3(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    # generics.GenericAPIView来获取
    # mixins.ListModelMixin查出所有数据列表
    # mixins.CreateModelMixin创建一条数据

    queryset = FirmList.objects.all()
    serializer_class = FirmListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Firms_detail3(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    # RetrieveModelMixin 查出一条数据
    # UpdateModelMixin更新一条数据
    # DestroyModelMixin删除一条数据

    queryset = FirmList.objects.all()
    serializer_class = FirmListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# -----------------------------------Django REST framework 混合模式mixins高级视图使用------------------------------

class Firms4(ListCreateAPIView):
    # ListCreateAPIView等价于帮我们实现mixins.ListModelMixin 和mixins.CreateModelMixin Retrieve
    queryset = FirmList.objects.all()
    serializer_class = FirmListSerializer


class Firms_detail4(RetrieveUpdateDestroyAPIView):
    # UpdateDestroyAPIView实现了对单挑纪录的增删改,相当于上面的mixins.RetrieveModelMixin， mixins.UpdateModelMixin，mixins.DestroyModelMixin
    queryset = FirmList.objects.all()
    serializer_class = FirmListSerializer


# -----------------------------------Django REST framework viewset使用------------------------------

class Firms5(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
             mixins.CreateModelMixin, mixins.DestroyModelMixin):
    # viewsets一个视图搞定对资源的所有的增删改查,使用viewsets下面GenericViewSet
    queryset = FirmList.objects.all()
    serializer_class = FirmListSerializer


# -----------------------------------Django REST framework viewset高级视图使用------------------------------

class Firms6(ModelViewSet):
    """
        list:
            查看所有的Firm信息
        create:
            创建一个Firm
        retrieve:
            获取一个Firm资源
        destroy:
            删除一个Firm资源
        update:
            更新一个Firm资源
        """
    queryset = FirmList.objects.all()
    serializer_class = FirmListSerializer
    # ModelViewSet: 读写，实现了mixins下面增删改查
    # 相当于
    # mixins.ListModelMixin,
    # mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.CreateModelMixin,
    # mixins.DestroyModelMixin
    #
    # ReadOnlyModelViewSet：只读，只实现了只读
