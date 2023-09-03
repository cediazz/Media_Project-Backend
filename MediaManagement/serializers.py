from rest_framework.serializers import ModelSerializer
from .models import Category,Plan,Coordinadas,Media,Field,Media_Fields

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class CoordinadasSerializer(ModelSerializer):
    class Meta:
        model = Coordinadas
        fields = '__all__'

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class FieldSerializer(ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class MediaFieldSerializer(ModelSerializer):

    field = FieldSerializer()
    class Meta:
        model = Media_Fields
        fields = '__all__'
