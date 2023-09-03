from rest_framework import viewsets, generics
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import action

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None


class PlanView(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    pagination_class = None


class CoordinadasView(viewsets.ModelViewSet):
    serializer_class = CoordinadasSerializer
    queryset = Coordinadas.objects.all()
    pagination_class = None


class MediaView(viewsets.ModelViewSet):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    pagination_class = None

    @action(detail=False, methods=['GET'])
    def get_medias(self, request):
        print(request.user)
        medias = Media.objects.all()
        media_serializers = MediaSerializerGet(medias, many=True)
        return Response(media_serializers.data)




class MediaContainerView(viewsets.ModelViewSet):
    serializer_class = MediaContainerSerializer
    queryset = MediaContainer.objects.all()
    pagination_class = None


class FieldView(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
    pagination_class = None





