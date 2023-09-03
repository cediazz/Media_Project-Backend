from rest_framework import viewsets, generics
from .serializers import *
from rest_framework.response import Response
from .models import *

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


class MediaFieldView(viewsets.ModelViewSet):
    serializer_class = MediaFieldSerializer
    queryset = Media_Fields.objects.all()
    pagination_class = None

    def create(self, request, *args, **kwargs):
        print(request.data)
        field = Field(name = request.data['field.name'])
        field.save()
        media = Media.objects.filter(id=request.data['media']).first()
        media_field = Media_Fields(media=media, field=field, field_value=request.data['field_value'])
        media_field.save()
        serializer = self.serializer_class(media_field)
        return Response(serializer.data)
        #return Response({'message': 'Creacion satisfactoria'}, status=status.HTTP_201_CREATED)


