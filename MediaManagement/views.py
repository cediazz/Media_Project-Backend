from rest_framework import viewsets, generics
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by('description')
    pagination_class = None


class PlanView(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.order_by('description')
    pagination_class = None


class CoordinadasView(viewsets.ModelViewSet):
    serializer_class = CoordinadasSerializer
    queryset = Coordinadas.objects.all()
    pagination_class = None


class MediaView(viewsets.ModelViewSet):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    pagination_class = None
    filterset_fields = {
        "description": ['exact'],
        'category__description': ['exact'],
        'plan__description': ['exact']
    }


    @action(detail=False, methods=['GET'])
    def get_media_view(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        pagination_class = PageNumberPagination()
        pagination_class.page_size = 2
        paginated_queryset = pagination_class.paginate_queryset(queryset,request)
        media_serializers = MediaSerializerGet(paginated_queryset, many=True)
        return pagination_class.get_paginated_response(media_serializers.data)

    @action(detail=False, methods=['GET'],serializer_class=Media_Fields_AllSerializer)
    def get_media_fields(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        media_serializers = Media_Fields_AllSerializer(queryset, many=True)
        return Response(media_serializers.data)



class Media_FieldView(viewsets.ModelViewSet):
    serializer_class = Media_FieldSerializer
    queryset = Media_Field.objects.all()
    pagination_class = None
    filterset_fields = {
        "media__description": ['exact'],

    }

    @action(detail=False, methods=['GET'])
    def get_media_field_view(self,request):
        queryset = self.filter_queryset(self.get_queryset())
        media_field_serializers = Media_FieldSerializerGet(queryset, many=True)
        return Response(media_field_serializers.data)

    @action(detail=False, methods=['GET','POST'], serializer_class=Media_FieldSerializerPost)
    def post_media_field_view(self, request):
        media_field_serializers = Media_FieldSerializerPost(data=request.data)
        if media_field_serializers.is_valid():
            media_field_serializers.save()
            return Response(media_field_serializers.data)
        return Response(media_field_serializers.errors)




class MediaContainerView(viewsets.ModelViewSet):
    serializer_class = MediaContainerSerializer
    queryset = MediaContainer.objects.all()
    pagination_class = None


class FieldView(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
    pagination_class = None





